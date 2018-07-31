#Flask app
#Run this scrip from the this file working directory
#set env variable FLASK_APP=flask_app.route0.py
#set env varibale FLASK_DEBUG=1 
#flask run
#go to the given ip address to see webApp

from flask import Flask

app = Flask(__name__) #new flask web application __name__ "this file name"

@app.route("/")
def index():
    return "Hello, World from Flask!!!"

@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"
