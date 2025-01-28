#pip install flask

from flask import Flask, request # Importing Flask and Request To Catch Request
import json # Import Json
from flask.templating import render_template # Importing Render Template To Server HTML Files

app = Flask(__name__) # Initialiazing App

@app.route("/", methods=["GET", "POST"]) # Creating Main Route
def home(): # Assinging a Function to the Route
    if request.method == "POST": # IF it is a post request
        name = request.form["name"] # Getting Input Name
        email = request.form["email"] # Getting Email
        password = request.form["password"] # Getting Password
        with open("filename.json", 'r') as json_file: # Opening The Json File as readable format
            data = json.load(json_file) # Storing Content of Json File In a Variable
            name_list = data["name"] # Getting Name List of Json File
            email_list = data["email"] # Getting Email List of Json File
            password_list = data["password"] # Getting Password List of Json File
            name_list.append(name) # Inserting Name Fetched From the HTML File to The List
            email_list.append(email) # Inserting Email Fetched From the HTML File to The List
            password_list.append(password) # Inserting Password Fetched From the HTML File to The List
        with open("filename.json", 'w') as container: # Opening Json File as writable format
            json.dump(data, container) # Storing the Previous Data with the New Inserted Data
    return render_template("index.html") # Returning Index.html

@app.route("/show-data") # Creating a New Route "/show-data"
def show_data(): # Assigning a funtion to the route
    with open("filename.json", 'r') as data_handler: # Opening the Json File as readable format
        all_data = json.load(data_handler) # Loading all contents of the json file to a variable
    name_list = all_data["name"] # Getting the List Of Name From the json File
    email_list = all_data["email"] # Getting the List of Email From the Json File
    password_list = all_data["password"] # Getting the List of Password From The Json File
    data = zip(name_list, email_list, password_list) # Creating a Zip Of All of the data and storing it in a variable
    return render_template("main.html", data=data) # Rendering the Template with the Data


app.run(debug=True, host="0.0.0.0") # Running the Flask app