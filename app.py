
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from ai import analyze_student

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    total = len(students)
    avg_attendance = sum([s['attendance'] for s in students]) / total if total else 0
    avg_score = sum([s['score'] for s in students]) / total if total else 0

    risk_count = sum(1 for s in students if analyze_student(s['score'], s['attendance'])[0] != "Low Risk")
    donut_data = [sum(1 for s in students if analyze_student(s['score'], s['attendance'])[0] == r)
                  for r in ["High Risk", "Medium Risk", "Low Risk"]]

    subjects = ["Math", "Science", "English"]
    subject_scores = [round(avg_score - 5 + i*3) for i in range(3)]  # Placeholder

    return render_template("dashboard.html",
                           total_students=total,
                           avg_attendance=round(avg_attendance, 2),
                           avg_score=round(avg_score, 2),
                           risk_count=risk_count,
                           donut_data=donut_data,
                           subjects=subjects,
                           subject_scores=subject_scores)

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    student_data = []
    for s in students:
        risk, tip = analyze_student(s['score'], s['attendance'])
        student_data.append(dict(s, risk=risk, tip=tip))

    return render_template('students.html', students=student_data)

if __name__ == '__main__':
    app.run(debug=True)
