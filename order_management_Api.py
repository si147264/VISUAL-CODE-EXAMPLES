import pyodbc
from flask import Flask, request, jsonify


connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=Order_ManagementDB;"
    "Trusted_Connection=yes;"
)
cursor = connection.cursor()
print("SQL is connected", cursor)
app = Flask(__name__)


@app.route('/Products', methods=["GET"])
def list_products():
    cursor.execute("SELECT * FROM Orders")
    rows = cursor.fetchall()
    products = []
    for row in rows:
        product = {
            "ID": row.ID,
            "Product_ID": row.Product_ID,
            "Quantity": row.Quantity,
            "Total_price": row.Total_price,
        }
        products.append(product)
    return jsonify(products)


@app.route('/Products', methods=["POST"])
def adding_order_info():
    data = request.get_json()

    cursor.execute("SELECT * FROM Products_ WHERE Product_ID = ?", data["Product_ID"])
    Product_id = cursor.fetchall()
    if Product_id is None:
        return jsonify({"error": "Invalid Product_ID"}), 400
    
    try:
        cursor.execute("INSERT INTO Orders(Product_ID, Quantity, Total_price) VALUES (?, ?, ?)", 
                       data["Product_ID"], data["Quantity"], data["Total_price"])
        
        connection.commit()
    except pyodbc.IntegrityError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(data), 201
@app.route('/Products/<int:ID>', methods=["PUT"]) 
def update_order_info(ID): 
    if request.method == "PUT": 
        data = request.get_json() 
        cursor.execute(""" UPDATE Orders SET Product_ID = ?, Quantity = ?,Total_price = ? WHERE ID = ? """, 
                       (data["Product_ID"], data["Quantity"], data["Total_price"], ID))
        connection.commit() 
        return jsonify({"message": "order is updated"}), 200
    
    
@app.route('/Products/<int:ID>', methods=["DELETE"])
def delete_appointment(ID):
    if request.method == "DELETE":
        cursor.execute("DELETE FROM Orders WHERE ID = ?", (ID,))
        connection.commit()
        return jsonify({"message": "Order info is deleted from list"}), 200






if __name__ == '__main__':
    app.run(debug=True)

