from flask import Flask,render_template,request
from api_file import get_weather_data
from sql_file import get_total_amount_spent,Get_the_customer_more_than_one_order,list_all_orders


app = Flask(__name__)


# CITY_NAME = "Hamirpur" # uncomment if you test this api on postman or other testing tools.

#############################################Task-1######################################################
# create a Api Endpoint fixed route.This api fetching the weather data from HTML UI form input.

@app.route('/weather/', methods=['GET']) #fetch api data using get method
def weather():
  city=request.args.get('city')
  
# Adding check to check the city enter or not in UI form input section.
  if not city:
      return render_template('index.html',data="City is required")
#using try and except block handle the exception.
  try:  
    data = get_weather_data(city)
    return render_template('index.html',data=data)
  except Exception as e:
    return{
      "status":"error",
      "message":"failed to fetch weather data",
      "details":str(e)
    }, 500
      

"""
   The commented code was written just to test the API in the first attempt using a single file.
   After successfully testing it, I planned to merge both tasks into one file.
   For this, I started organizing the project using a hierarchical file structure.
   
"""
"""
You can uncomment the beloe function .if you want to test this api on tools like Postman Agent
"""
# def weather():
#     try:
#         data,status_code=get_weather_data(CITY_NAME)
#         print(".........",data)
#         if status_code == 200:
#           return {
#             "status":"success",
#             "data":data
#             }, 200 
#           #  Return actual weather data as JSON
#         else:
#           return {"message": "Failed to fetch weather data"}
#     except Exception as e:
#         return   {"error":"Failed to fetch weather data","details":str(e)}, 500

####################################################Task-2##########################################################
"""
If you are using XAMPP or another connection IDE, 
simply go to the SQL file and configure the database settings according to your system.
Then, uncomment the API code, run the file, and view the output in your browser.
You see the Result of this api in /screenshot folder.
"""
# @app.route('/task2/',methods=['GET'])
# def SQL_queries():
#   query_1=get_total_amount_spent()
#   print("Get the total amount spent by each customer......",query_1)
#   query_2=Get_the_customer_more_than_one_order()
#   print("List all orders placed after '2023-01-03.........",query_2)
#   query_3=list_all_orders()
#   print("Get the customer(s) who made more than one order..........",query_3)
#   return {
#     "data1":query_1,"data2":query_2,"data3":query_3
#   }, 200


if __name__ == '__main__':
    app.run(debug=True, port=8800, host='0.0.0.0')
   