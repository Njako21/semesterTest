from opcua_client import connect, is_connected
from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from brew_post import brew_post
from read import allRead
from write import writer
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
connect()

#if in doubt start the server and connect to the ip in a browser

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

@app.route("/api")
@app.route("/api/")
@app.route("/")
def doesNotExist():
    return render_template('api.html')


app.register_blueprint(brew_post)
app.register_blueprint(allRead)
app.register_blueprint(writer)


if __name__ == '__main__':
    app.run(port=5000)
