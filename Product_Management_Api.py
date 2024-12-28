import pyodbc
from flask import Flask, request, jsonify

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=PD;"
    "Trusted_Connection=yes;"
)
cursor = connection.cursor()
print("SQL is connected", cursor)

app = Flask(__name__)

@app.route('/Products', methods=["GET"])
def list_appointments():
    cursor.execute("SELECT * FROM Product_Management")  
    rows = cursor.fetchall()
    products = []
    for row in rows:
        product = {
            "ID": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "stock_quantity": row[4]
        }
        products.append(product)
    return jsonify(products)

@app.route('/Products', methods=["POST"])
def add_new_product():
    data = request.get_json()  
    cursor.execute(
        "INSERT INTO  Product_Management( name,description,price,stock_quantity) VALUES (?,?,?, ?)",
        (data["name"], data["description"],data["price"],data["stock_quantity"])
    )
    connection.commit() 
    return jsonify({"message": "New product info is added into product list successfully!"}), 201


@app.route('/Products/<int:ID>', methods=["PUT"]) 
def update_product(ID):
 data = request.get_json() 
 cursor.execute( "UPDATE Product_Management SET name=?, description=?, price=?, stock_quantity=? WHERE ID=?", 
                (data["name"], data["description"], data["price"], data["stock_quantity"], ID) )
 connection.commit() 
 return jsonify({"message": "Product in category list is updated"}), 200

@app.route('/Products/<int:ID>', methods=["DELETE"])
def delete_appointment(ID):
    if request.method == "DELETE":
        cursor.execute("DELETE FROM Product_Management WHERE ID = ?", (ID,))
        connection.commit()
        return jsonify({"message": "Appointment is deleted from list"}), 200
if __name__ == '__main__':
    app.run(debug=True)
