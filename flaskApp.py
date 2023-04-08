from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/404")
def page_not_found():
    return render_template("404_error.html")
