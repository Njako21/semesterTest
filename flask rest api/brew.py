import math

from flask import Blueprint, make_response, jsonify, render_template, request
from prefixs.prefixs import brew as prefix
from opcua_client import read_node_val
from variables.brew import BREW, control_cmd

brew = Blueprint('brew', __name__, template_folder='templates')

@brew.route(prefix + "/read/<string:brew_info>", methods=['GET'])
def brew_read(brew_info):
    try:
        if brew_info == "all":
            return all()
        elif brew_info == "set_command" and int(math.floor(float(read_node_val(BREW[brew_info])))) != 0:
            value = int(math.floor(float(read_node_val(BREW[brew_info]))))
            response = jsonify({brew_info: control_cmd[value]})
        else:
            response = jsonify({brew_info: read_node_val(BREW[brew_info])})
        return make_response(response, 200)
    except:
        return does_not_exist_brew_read

@brew.route(prefix + "/write/<string:brew_info>", methods=['POST', 'GET'])
def brew_write(brew_info):
    request_body = request.get_json()
    print(request_body)
    print("hello world")
    return make_response(jsonify({
        "geta": "test",
    }))
    try:
        if brew_info == "all":
            return all()
        response = jsonify({brew_info: read_node_val(BREW[brew_info])})
        return make_response(response, 200)
    except:
        return does_not_exist_brew_write

@brew.route(prefix+"/read")
@brew.route(prefix+"/read/")
def does_not_exist_brew_read():
    return render_template('read.html', items=BREW.keys(), subdomain=(prefix+"/read"), all=True, example="set_speed")

@brew.route(prefix + "/<string:brew_info>", methods=['GET'])
@brew.route(prefix)
@brew.route(prefix+"/")
def does_not_exist_brew():
    return render_template('brew.html')

@brew.route(prefix+"/write")
@brew.route(prefix+"/write/")
def does_not_exist_brew_write():
    return render_template('write.html', items=BREW.keys(), subdomain=(prefix+"/write"), all=True, example="set_speed")

def all():
    temp = BREW.copy()

    for key in BREW:
        temp[key] = read_node_val(temp[key])
    return make_response(jsonify(temp), 200)

@brew.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response

