from opcua_client import connect, is_connected
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from inventory import inventory
from defaultRoutes import defRoutes
from Admin import admin
from batch import batch
from brew import brew
from machine import machine
from brew_post import brew_post

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
connect()

@app.before_request
def before_request():
    if not is_connected():
        if request.method == 'POST':
            connect()
            redirect("/")
            if(is_connected()):
                return "Connected successfully please refresh"
            else:
                return "Could not connect please refresh"
        elif request.method == 'GET':
            return render_template("no_connection.html")


app.register_blueprint(inventory)
app.register_blueprint(defRoutes)
app.register_blueprint(admin)
app.register_blueprint(batch)
app.register_blueprint(brew)
app.register_blueprint(machine)
app.register_blueprint(brew_post)


if __name__ == '__main__':
    app.run(port=5000)
