from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/version")
def exampleDict():
    return {"name":"flask", "version":3}

@app.route("/test")
def test():
    return "Exito",201

@app.route("/headers")
def headers():
    return {"status":False},404,{"custom": "flask"}