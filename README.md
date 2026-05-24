📸 Smart Attendance System

An AI-powered Smart Attendance System that automates attendance tracking using face recognition technology. The system detects and recognizes student faces in real-time and automatically marks attendance while storing records in a MySQL database.

This project combines Computer Vision, Python, Streamlit, and Database Management to create an efficient and modern attendance management solution.

🚀 Features

✅ Real-time face detection and recognition
✅ Automated attendance marking
✅ Prevents duplicate attendance entries
✅ MySQL database integration
✅ Interactive Streamlit dashboard
✅ Attendance history tracking
✅ Student record management
✅ Clean and user-friendly interface

🧠 Project Overview

Traditional attendance systems are time-consuming and prone to manual errors. This Smart Attendance System uses AI-based face recognition to identify students automatically and mark attendance instantly.

The system:

Detects faces using OpenCV
Recognizes registered students
Stores attendance records in MySQL
Displays attendance data through Streamlit UI
🏗️ System Architecture
Camera Input → Face Detection → Face Recognition → Attendance Validation → MySQL Database → Streamlit Dashboard
🛠️ Tech Stack
Programming Language
Python
Frontend/UI
Streamlit
Computer Vision
OpenCV
NumPy
Pillow
Database
MySQL
mysql-connector-python
Data Handling
Pandas
📂 Project Structure
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
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/smart-attendance-system.git
cd smart-attendance-system
2️⃣ Create Virtual Environment
python -m venv smart_env

Activate virtual environment:

Windows
smart_env\Scripts\activate
macOS/Linux
source smart_env/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure MySQL Database

Create a MySQL database:

CREATE DATABASE SmartAttendance;

Update database credentials in:

config/db_config.py

or inside:

app.py

Example:

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3307,
    "user": "root",
    "password": "your_password",
    "database": "SmartAttendance"
}
▶️ Run the Application
streamlit run app.py

Application runs on:

http://localhost:8501
📸 How It Works
Student images are stored in the dataset folder
The camera captures live video
Faces are detected and matched
Attendance is marked automatically
Duplicate entries are prevented
Attendance logs are stored in MySQL
Dashboard displays attendance records
🗄️ Database Tables
Students Table

Stores registered student details.

Column	Description
StudentID	Unique student ID
Name	Student name
ImagePath	Path to student image
AttendanceLog Table

Stores attendance records.

Column	Description
LogID	Attendance log ID
StudentID	Student ID
Name	Student name
Date	Attendance date
Time	Attendance time
🌟 Key Functionalities
🎯 Face Recognition

Uses OpenCV-based face recognition to identify students from the dataset.

📝 Attendance Marking

Automatically records attendance in the database.

🚫 Duplicate Prevention

Ensures attendance is marked only once per student per day.

📊 Attendance Dashboard

Displays attendance logs using Streamlit.

📸 Screenshots
Dashboard

Add dashboard screenshot here

Attendance Detection

Add face recognition screenshot here

Attendance Records

Add attendance table screenshot here

🔥 Future Enhancements
Deep Learning-based face recognition
Multi-face attendance detection
Admin authentication system
Attendance analytics dashboard
Cloud database integration
CSV/PDF report export
Real-time notifications
Mobile app integration
Face mask detection support
💡 Learning Outcomes

This project helped in understanding:

Computer Vision concepts
Face recognition workflows
OpenCV integration
Database operations with MySQL
Streamlit application development
Real-time data processing
Python project structuring
Full project deployment workflow
🤝 Contributing

Contributions are welcome.

Fork the repository
Create a feature branch
Commit your changes
Push to your branch
Open a Pull Request
📄 License

This project is licensed under the MIT License.

👩‍💻 Author

Madhuri H S

GitHub: https://github.com/MADHURI-HS
Passionate about AI, Full Stack Development, and Computer Vision
