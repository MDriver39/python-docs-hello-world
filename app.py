from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! It is MDriver3 From the VIP3-Club"
