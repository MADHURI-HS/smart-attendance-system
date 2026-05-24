# 📸 Smart Attendance System

An AI-powered Smart Attendance System that automates attendance tracking using face recognition technology. The system detects and recognizes student faces in real-time and automatically marks attendance while storing records in a MySQL database.

This project combines Computer Vision, Python, Streamlit, and Database Management to create an efficient and modern attendance management solution.

---

# 🚀 Features

✅ Real-time face detection and recognition
✅ Automated attendance marking
✅ Prevents duplicate attendance entries
✅ MySQL database integration
✅ Interactive Streamlit dashboard
✅ Attendance history tracking
✅ Student record management
✅ Clean and user-friendly interface

---

# 🧠 Project Overview

Traditional attendance systems are time-consuming and prone to manual errors. This Smart Attendance System uses AI-based face recognition to identify students automatically and mark attendance instantly.

The system:

1. Detects faces using OpenCV
2. Recognizes registered students
3. Stores attendance records in MySQL
4. Displays attendance data through Streamlit UI

---

# 🏗️ System Architecture

```text
Camera Input → Face Detection → Face Recognition → Attendance Validation → MySQL Database → Streamlit Dashboard
```

---

# 🛠️ Tech Stack

## Programming Language

* Python

## Frontend/UI

* Streamlit

## Computer Vision

* OpenCV
* NumPy
* Pillow

## Database

* MySQL
* mysql-connector-python

## Data Handling

* Pandas

---

# 📂 Project Structure

```bash
attendance_tracker/
│
├── app.py                       # Main Streamlit application
├── main.py                      # Entry point
├── requirements.txt             # Project dependencies
│
├── recognition/
│   └── recognizer.py            # Face recognition logic
│
├── database/
│   ├── db_connection.py         # Database connection
│   └── attendance_service.py    # Attendance operations
│
├── config/
│   └── db_config.py             # Database configuration
│
├── dataset/                     # Student image dataset
│
└── smart_env/                   # Virtual environment (not recommended for GitHub)
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-attendance-system.git
```

```bash
cd smart-attendance-system
```

---

# 2️⃣ Create Virtual Environment

```bash
python -m venv smart_env
```

Activate virtual environment:

### Windows

```bash
smart_env\Scripts\activate
```

### macOS/Linux

```bash
source smart_env/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Configure MySQL Database

Create a MySQL database:

```sql
CREATE DATABASE SmartAttendance;
```

Update database credentials in:

```bash
config/db_config.py
```

or inside:

```bash
app.py
```

Example:

```python
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "your_password",
    "database": "SmartAttendance"
}
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Application runs on:

```bash
http://localhost:8501
```

---

# 📸 How It Works

1. Student images are stored in the dataset folder
2. The camera captures live video
3. Faces are detected and matched
4. Attendance is marked automatically
5. Duplicate entries are prevented
6. Attendance logs are stored in MySQL
7. Dashboard displays attendance records

---

# 🗄️ Database Tables

## Students Table

Stores registered student details.

| Column    | Description           |
| --------- | --------------------- |
| StudentID | Unique student ID     |
| Name      | Student name          |
| ImagePath | Path to student image |

---

## AttendanceLog Table

Stores attendance records.

| Column    | Description       |
| --------- | ----------------- |
| LogID     | Attendance log ID |
| StudentID | Student ID        |
| Name      | Student name      |
| Date      | Attendance date   |
| Time      | Attendance time   |

---

# 🌟 Key Functionalities

## 🎯 Face Recognition

Uses OpenCV-based face recognition to identify students from the dataset.

## 📝 Attendance Marking

Automatically records attendance in the database.

## 🚫 Duplicate Prevention

Ensures attendance is marked only once per student per day.

## 📊 Attendance Dashboard

Displays attendance logs using Streamlit.

---

# 📸 Screenshots

## Dashboard

*Add dashboard screenshot here*

## Attendance Detection

*Add face recognition screenshot here*

## Attendance Records

*Add attendance table screenshot here*

---

# 🔥 Future Enhancements

* Deep Learning-based face recognition
* Multi-face attendance detection
* Admin authentication system
* Attendance analytics dashboard
* Cloud database integration
* CSV/PDF report export
* Real-time notifications
* Mobile app integration
* Face mask detection support

---

# 💡 Learning Outcomes

This project helped in understanding:

* Computer Vision concepts
* Face recognition workflows
* OpenCV integration
* Database operations with MySQL
* Streamlit application development
* Real-time data processing
* Python project structuring
* Full project deployment workflow

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Madhuri H S**

* GitHub: [https://github.com/MADHURI-HS](https://github.com/MADHURI-HS)
* Passionate about AI, Full Stack Development, and Computer Vision

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
