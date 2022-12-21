from opcua_client import read_node_val
from flask import Blueprint, jsonify, make_response, render_template
from variables.all import ALL
from prefixs.prefixs import read as prefix

allRead = Blueprint('allRead', __name__, template_folder='templates')

@allRead.route(prefix + "/<string:string>")
def ingredient(string):
    try:
        items = string.split(":")
        temp = ALL.copy()
        temp2 = {}
        for item in items:
            temp2[item] = read_node_val(temp[item])
            return make_response(jsonify(temp2), 200)
    except:
        return make_response(jsonify({string: "does not exist"}), 404)


@allRead.route(prefix)
@allRead.route(prefix + "/")
def does_not_exist_brew_write():
    return render_template('read.html', items=ALL.keys(), subdomain=(prefix), all=True, example="hops:yeast")

@allRead.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost"
    return response