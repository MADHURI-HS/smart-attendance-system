# app.py

import streamlit as st
import cv2
import pandas as pd
import mysql.connector
from datetime import datetime
from recognition.recognizer import detect_faces

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart Attendance System",
    page_icon="📸",
    layout="wide"
)

# ==========================================
# DATABASE CONFIG
# ==========================================

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "root123",
    "database": "SmartAttendance"
}

# ==========================================
# DATABASE CONNECTION
# ==========================================

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ==========================================
# CREATE TABLES
# ==========================================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # Students Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INT PRIMARY KEY,
            Name VARCHAR(100),
            ImagePath VARCHAR(255)
        )
    """)

    # Attendance Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS AttendanceLog (
            LogID INT PRIMARY KEY AUTO_INCREMENT,
            StudentID INT,
            Name VARCHAR(100),
            Date DATE,
            Time TIME
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()

# ==========================================
# MARK ATTENDANCE
# ==========================================

def mark_attendance(student_id, name):

    conn = get_connection()
    cursor = conn.cursor()

    today = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    # Duplicate Check
    cursor.execute("""
        SELECT *
        FROM AttendanceLog
        WHERE StudentID=%s
        AND Date=%s
    """, (student_id, today))

    result = cursor.fetchone()

    if result:
        cursor.close()
        conn.close()
        return False

    # Insert Attendance
    cursor.execute("""
        INSERT INTO AttendanceLog
        (StudentID, Name, Date, Time)
        VALUES (%s, %s, %s, %s)
    """, (
        student_id,
        name,
        today,
        current_time
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return True

# ==========================================
# FETCH ATTENDANCE
# ==========================================

def fetch_attendance():

    conn = get_connection()

    query = """
        SELECT *
        FROM AttendanceLog
        ORDER BY LogID DESC
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# ==========================================
# FETCH STUDENTS
# ==========================================

def fetch_students():

    conn = get_connection()

    query = """
        SELECT *
        FROM Students
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df

# ==========================================
# CREATE TABLES ON START
# ==========================================

create_tables()

# ==========================================
# SESSION STATE
# ==========================================

if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

if "last_message" not in st.session_state:
    st.session_state.last_message = ""

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Register Student",
        "Start Attendance",
        "Attendance Records"
    ]
)

# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.title("📊 Smart Attendance Dashboard")

    attendance_df = fetch_attendance()
    students_df = fetch_students()

    total_students = len(students_df)

    total_logs = len(attendance_df)

    today = datetime.now().strftime('%Y-%m-%d')

    today_attendance = len(
        attendance_df[
            attendance_df["Date"].astype(str)
            == today
        ]
    ) if not attendance_df.empty else 0

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Students",
        total_students
    )

    col2.metric(
        "Today's Attendance",
        today_attendance
    )

    col3.metric(
        "Total Attendance Logs",
        total_logs
    )

    st.subheader("📋 Recent Attendance")

    if attendance_df.empty:
        st.warning(
            "No attendance records found"
        )

    else:
        st.dataframe(
            attendance_df,
            use_container_width=True
        )

# ==========================================
# REGISTER STUDENT PAGE
# ==========================================

elif page == "Register Student":

    st.title("🧑 Register Student")

    student_id = st.text_input(
        "Student ID"
    )

    student_name = st.text_input(
        "Student Name"
    )

    uploaded_file = st.file_uploader(
        "Upload Student Image",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("Register Student"):

        if (
            student_id and
            student_name and
            uploaded_file
        ):

            # Save Image
            image_path = (
                f"dataset/{student_id}.jpg"
            )

            with open(image_path, "wb") as f:
                f.write(uploaded_file.read())

            # Insert into Database
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO Students
                (StudentID, Name, ImagePath)
                VALUES (%s, %s, %s)
            """, (
                student_id,
                student_name,
                image_path
            ))

            conn.commit()

            cursor.close()
            conn.close()

            st.success(
                f"{student_name} registered successfully"
            )

        else:
            st.error(
                "Please fill all fields"
            )

    st.subheader("📋 Registered Students")

    students_df = fetch_students()

    if students_df.empty:
        st.warning(
            "No students registered"
        )

    else:
        st.dataframe(
            students_df,
            use_container_width=True
        )

# ==========================================
# START ATTENDANCE PAGE
# ==========================================

elif page == "Start Attendance":

    st.title("📸 Start Attendance")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶ Start Camera"):
            st.session_state.camera_running = True

    with col2:
        if st.button("⏹ Stop Camera"):
            st.session_state.camera_running = False

    FRAME_WINDOW = st.image([])

    if st.session_state.camera_running:

        camera = cv2.VideoCapture(0)

        if not camera.isOpened():

            st.error(
                "Unable to access camera"
            )

        else:

            st.success("Camera Started")

            while st.session_state.camera_running:

                ret, frame = camera.read()

                if not ret:
                    st.error(
                        "Failed to capture frame"
                    )
                    break

                faces = detect_faces(frame)

                for (x, y, w, h) in faces:

                    # Draw Rectangle
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )

                    # Fetch Student Dynamically
                    conn = get_connection()
                    cursor = conn.cursor()

                    cursor.execute("""
                        SELECT StudentID, Name
                        FROM Students
                        LIMIT 1
                    """)

                    student = cursor.fetchone()

                    cursor.close()
                    conn.close()

                    if student:

                        student_id = student[0]
                        name = student[1]

                        attendance_marked = (
                            mark_attendance(
                                student_id,
                                name
                            )
                        )

                        # Display Name
                        cv2.putText(
                            frame,
                            name,
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 255, 0),
                            2
                        )

                        # Message Handling
                        if attendance_marked:

                            message = (
                                f"Attendance Marked for {name}"
                            )

                        else:

                            message = (
                                f"{name} already marked today"
                            )

                        # Prevent Repeated Messages
                        if (
                            st.session_state.last_message
                            != message
                        ):

                            if attendance_marked:
                                st.success(message)
                            else:
                                st.warning(message)

                            st.session_state.last_message = (
                                message
                            )

                # Convert BGR to RGB
                frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                FRAME_WINDOW.image(
                    frame,
                    channels="RGB"
                )

            camera.release()
            cv2.destroyAllWindows()

# ==========================================
# ATTENDANCE RECORDS PAGE
# ==========================================

elif page == "Attendance Records":

    st.title("📋 Attendance Records")

    attendance_df = fetch_attendance()

    if attendance_df.empty:

        st.warning(
            "No attendance records found"
        )

    else:

        st.dataframe(
            attendance_df,
            use_container_width=True
        )

        # CSV Download
        csv = attendance_df.to_csv(
            index=False
        ).encode('utf-8')

        st.download_button(
            label="⬇ Download Attendance CSV",
            data=csv,
            file_name='attendance.csv',
            mime='text/csv'
        )