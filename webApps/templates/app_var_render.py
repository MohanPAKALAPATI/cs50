from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    headline_render_var = "Hellow World thru headline render var"
    return render_template("index.html", headline = headline_render_var)
