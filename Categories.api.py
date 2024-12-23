import pyodbc
from flask import Flask, request, jsonify

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=My_categories ;"
    "Trusted_Connection=yes;"
)

cursor=connection.cursor()
print("SQL is connected")
app = Flask(__name__)

@app.route('/categories', methods=["GET"])
def show():
    cursor.execute("SELECT * FROM categoriess")
    rows = cursor.fetchall()
    categories = [{"ID": row[0], "Name": row[1], "Description":row[2]} for row in rows]
    
    return jsonify(categories)



@app.route('/categories', methods=["POST"])
def add_new_product():
    data = request.get_json()  
    cursor.execute(
        "INSERT INTO  categoriess(ID, Name,Description) VALUES (?,?, ?)",
        (data["ID"],data["Name"], data["Description"])
    )
    connection.commit() 
    return jsonify({"message": "New product info is added into user list successfully!"}), 201

@app.route('/categories/<int:ID>', methods=["PUT"])
def update_product(ID):
    data = request.get_json()
    cursor.execute(
        "UPDATE categoriess SET Name=?, Description=? WHERE ID=?",
        (data.get("Name"), data.get("Description"), ID)
    )
    connection.commit()
    return jsonify({"message": "Product in category list is updated"}), 200




