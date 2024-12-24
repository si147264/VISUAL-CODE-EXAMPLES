import pyodbc
from flask import Flask ,jsonify,request
connection=pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=Bookmanagement;"
    "Trusted_Connection=yes;")


cursor=connection.cursor()
print("SQL connection is connected",cursor)

app = Flask(__name__)
@app.route("/Books",methods=["GET"])
def taking_books():
    if request.method=="GET":
        cursor.execute("SELECT *FROM bookmanagement")
        rows=cursor.fetchall()
        books=[]
        for row in rows:
            book={"ID":row[0],"Name":row[1],"Description":row[2],"Price":row[3],"Stock_quantity":row[4]}
            books.append(book)
        return jsonify(books)
@app.route("/Books", methods=["POST"])
def adding_book():
    if request.method == "POST":
        data = request.get_json()
        
        cursor.execute(
                "INSERT INTO bookmanagement(ID,Name, Description, Price, Stock_quantity) VALUES(?,?,?,?,?)",
                (data["ID"],data["Name"],data["Description"], data["Price"], data["Stock_quantity"])
            )
        connection.commit()
        return jsonify({"message": f"{data['Name']} book is added to the book management list."}), 201
@app.route("/Books/<int:ID>", methods=["PUT"])
def update_book(ID):
    if request.method == "PUT":
        data = request.get_json()

        
        cursor.execute("UPDATE bookmanagement SET Name=?, Description=?, Price=?, Stock_quantity=? WHERE ID=?", 
                       (data["Name"], data["Description"], data["Price"], data["Stock_quantity"], ID))
        
     
        connection.commit()

    
        return jsonify({"message": f"{data['Name']} is updated"}), 200
    
@app.route("/Books/<int:ID>", methods=["DELETE"])
def delete(ID):
    if request.method == "DELETE":
        
        cursor.execute("DELETE FROM bookmanagement WHERE ID=?", (ID,))
        connection.commit()
        return jsonify({"message": f"{ID} is deleted"}), 200



if __name__ == '__main__':
    app.run(debug=True)

