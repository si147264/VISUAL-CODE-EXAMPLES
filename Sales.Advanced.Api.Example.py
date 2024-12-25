import pyodbc
from flask import Flask, request, jsonify

connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=VIVOBOOK\\SQLEXPRESS;"
    "Database=Sales;"
    "Trusted_Connection=yes;"
)
cursor = connection.cursor()
print("SQL is connected", cursor)


app = Flask(__name__)

@app.route("/Mysales/report", methods=["GET"])
def take_sale_report():
    try:
        start_date = request.args.get("start_date", "2025-01-01")
        final_date = request.args.get("final_date", "2027-01-01")

        query = """SELECT * FROM sales WHERE Saledate BETWEEN ? AND ?"""
        cursor.execute(query, (start_date, final_date))
        my_sales = cursor.fetchall()

        total_amount = sum(row.Amount for row in my_sales)
        print(total_amount)

        sale_info = [{
            "Saledate": row.Saledate, "Amount": row.Amount}
            for row in my_sales
        ]
        return jsonify({"sales": sale_info, "total_amount": total_amount})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
   app.run(debug=True)
