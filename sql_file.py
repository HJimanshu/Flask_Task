from flask import Flask
import mysql.connector

app = Flask(__name__)

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="demo"
)

def get_total_amount_spent():
   cursor = db.cursor(dictionary=True)
   query= """
            SELECT customer_id, SUM(amount) AS total_spent
            FROM orders
            GROUP BY customer_id;
     """
   cursor.execute(query)
   results=cursor.fetchall()
   cursor.close()
   return {"Get the total amount spent by each customer":results}  

def list_all_orders():
   cursor = db.cursor(dictionary=True)
   query="""
   SELECT *  FROM orders
   WHERE order_date > '2023-01-03';
   """
   cursor.execute(query)
   results=cursor.fetchall()
   cursor.close()
   return {"List all orders placed after '2023-01-03'":results}  

def Get_the_customer_more_than_one_order():
   cursor = db.cursor(dictionary=True)
   query="""SELECT customer_id, COUNT(*) AS order_count FROM orders
        GROUP BY customer_id HAVING COUNT(*) > 1;
   """
   cursor.execute(query)
   results=cursor.fetchall()
   cursor.close()
   return {"Get the customer(s) who made more than one order":results}  
   

if __name__ == '__main__':
    app.run(debug=True)
