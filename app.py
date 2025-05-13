from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Smart Attendance System</h1><p><a href='/attendance'>View Attendance</a></p>"

@app.route('/attendance')
def show_attendance():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, date, time FROM attendance ORDER BY id DESC")
    records = cursor.fetchall()
    conn.close()
    return render_template("attendance.html", records=records)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

