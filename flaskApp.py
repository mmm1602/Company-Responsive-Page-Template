from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(r"/HTML/index.html")

app.run(host="0.0.0.0", port=80)