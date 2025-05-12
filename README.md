# Smart Facial Recognition Attendance System

This project is a Flask-based smart attendance tracking system that uses OpenCV for face detection and simulated face recognition. Student attendance is stored in an SQLite database and displayed through a clean web interface.

## Features
- Face detection with OpenCV
- Simulated face recognition for testing
- Attendance logging with date and time
- SQLite database storage
- Flask web interface to view attendance
- Ready for deployment on Render

## Requirements
- Python 3.8–3.11 (recommended)
- Flask
- OpenCV
- SQLite3

## How to Run
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```
   python init_db.py
   ```
4. Start the application:
   ```
   python app.py
   ```
5. Open your browser to `http://127.0.0.1:5000/`

## Notes
- Simulated recognition can be switched between students by editing `simple_face_detector.py`
- Ideal for prototyping and final-year student projects
