from flask import Flask, jsonify, render_template, request

from models.calculator import calculate

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("index.html")

@app.post("/calculate")
def calculate_route():
    data = request.get_json(silent=True) or {}
    result = calculate(data.get("expression", ""))
    return jsonify(result=result)
