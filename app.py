from flask import Flask 

app = Flask(__name__)

@app.route("/")

def calculator():
    return "<h1>Hello estoy probando flask soy annita</h1>"
