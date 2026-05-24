from datetime import datetime
from database.db_connection import get_connection

class AttendanceService:

    @staticmethod
    def mark_attendance(person_id, name):

        conn = None
        cursor = None

        try:
            conn = get_connection()
            cursor = conn.cursor()

            today = datetime.now().strftime('%Y-%m-%d')
            current_time = datetime.now().strftime('%H:%M:%S')

            # Duplicate Check
            query = """
                SELECT LogID
                FROM AttendanceLog
                WHERE PersonID=%s AND Date=%s
            """

            cursor.execute(query, (person_id, today))

            if cursor.fetchone():
                print(f"{name} attendance already marked today.")
                return False

            # Insert Attendance
            insert_query = """
                INSERT INTO AttendanceLog
                (PersonID, Name, Date, Time)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                insert_query,
                (person_id, name, today, current_time)
            )

            conn.commit()

            print(f"Attendance marked for {name}")
            return True

        except Exception as e:
            print("Database Error:", e)
            return False

        finally:
            if cursor:
                cursor.close()

            if conn and conn.is_connected():
                conn.close()