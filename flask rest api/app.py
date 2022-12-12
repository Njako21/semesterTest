from opcua_client import changeIp, connect
from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS
from inventory import inventory
from defaultRoutes import defRoutes
from Admin import admin
from batch import batch
from brew import brew
from machine import machine
def start():
    user_input = input("Use pre set ip and port \n Y or N: ")
    if user_input.strip().lower() == "n":
        ip = input("ip:").strip()
        if ":" not in ip:
            port = input("port: ").strip()

        if input("Connect with ip\n" + ip + "\n" + port + "\nY or N: ").lower() == "y":
            changeIp(ip, port)
        else:
            start()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

connect()

app.register_blueprint(inventory)
app.register_blueprint(defRoutes)
app.register_blueprint(admin)
app.register_blueprint(batch)
app.register_blueprint(brew)
app.register_blueprint(machine)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response

if __name__ == '__main__':
    app.run(port=5000)
