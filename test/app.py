from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = db.cursor()

@app.route('/')
def index():
    # Fetch student data from MySQL
    cursor.execute("SELECT id, student_name, cgpa FROM students")
    students = cursor.fetchall()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
