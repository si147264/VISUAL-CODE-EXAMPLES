import pyodbc
from flask import Flask, jsonify, request

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=Student_management;"
    "Trusted_Connection=yes;"
)

cursor = connection.cursor()
print("SQL connection is connected", cursor)

app = Flask(__name__)


@app.route("/Students", methods=["GET"])
def get_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    student_list = []
    for row in rows:
        student = {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "enrollment_date": row[4]
        }
        student_list.append(student)
    return jsonify(student_list)


@app.route("/Students", methods=["POST"])
def add_student():
    data = request.get_json()
    cursor.execute(
        "INSERT INTO student( first_name, last_name, email, enrollment_date) VALUES(?,?,?,?)",
        ( data["first_name"], data["last_name"], data["email"], data["enrollment_date"])
    )
    connection.commit()
    return jsonify({
        "message": f"Student {data['first_name']} {data['last_name']} is added to the student list."
    }), 201

@app.route("/Students/<int:id>", methods=["PUT"])
def update_studentinfo(id):
    if request.method == "PUT":
        data = request.get_json()

        
        cursor.execute("UPDATE student SET first_name=?, last_name=?, email=?, enrollment_date=? WHERE id=?", 
                         ( data["first_name"], data["last_name"], data["email"], data["enrollment_date"], id))
        
     
        connection.commit()

    
        return jsonify({"message": f"{data['first_name']} is updated"}), 200
@app.route("/Students/<int:id>", methods=["DELETE"])
def delete(id):
    if request.method == "DELETE":
        
        cursor.execute("DELETE FROM student WHERE id=?", (id,))
        connection.commit()
        return jsonify({"message": f"{id} is deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)

