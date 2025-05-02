**Flask Task Assignment – Python API & SQL Query**

Hi, I’m Himanshu.
In this project, I used the Flask framework and followed the official documentation here:
👉 [Flask Quickstart Guide](https://flask.palletsprojects.com/en/stable/quickstart/)

This repository contains my assignment task implementation. Below, I have explained all the steps required to set up and run this project successfully.

🚀 **Getting Started**
1. Clone the Repository
  > git clone https://github.com/HJimanshu/Flask_Task.git

  > cd Flask_Task

  > git status  # to verify your clone

2. Set Up Virtual Environment
  > python -m venv myenv

3. Install Dependencies
  > pip install -r requirements.txt

4. Run the Server
  > python main.py


🧪 **Task 1 – Weather API**

1.Test via Postman

Method: GET

URL: http://127.0.0.1:8800/weather/

# Params:
  key: city
  value: {city_name}

2.Test via Browser (HTML Interface) 

 Open the following URL in your browser:
 
  > http://127.0.0.1:8800/weather/

This loads an HTML page where you can enter a city name in the input field and click the Search button to see the current weather of the specified city.

✅ This also fulfills Additional Task 3.


**Task 2 – SQL Task**

For this task, a Flask API was created to interact with a mock MySQL table named orders.

Since my personal system is currently unavailable for use, I am working on another desktop that has XAMPP installed. Therefore, I followed a standard approach by:

> Setting up DB configuration for MySQL

> Writing all SQL queries inside a dedicated function

> Creating a separate API endpoint in main.py to run these queries

**Setup Instructions**

1.Make sure your local MySQL server (via XAMPP or another IDE) is running.

2.Configure your database connection details in sql_file.py.

3.Uncomment the /task2/ API route in main.py.

4.Start the server:

> python main.py

5.Test in your browser:

> http://127.0.0.1:8800/task2/

# This will return the output of all three SQL queries in JSON format.

