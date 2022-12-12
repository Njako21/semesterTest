import math

from flask import Blueprint, render_template, jsonify, make_response
from opcua_client import read_node_val
from prefixs.prefixs import machine as prefix
from variables.machine import MACHINE,status
machine = Blueprint('machine', __name__, template_folder='templates')

@machine.route(prefix + "/<string:machine_data>")
def machineD(machine_data):
    try:
        if machine_data == "current_state":
            value = int(math.floor(float(read_node_val(MACHINE[machine_data]))))
            response = jsonify({machine_data: status[value]})
        else:
            response = jsonify({machine_data: read_node_val(MACHINE[machine_data])})

        return make_response(response, 200)
    except:
        return doesNotExist()


@machine.route(prefix)
@machine.route(prefix+"/")
def doesNotExist():
    return render_template('machine.html', machine_links=MACHINE.keys())


@machine.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response