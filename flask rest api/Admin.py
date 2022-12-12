import math

from flask import Blueprint, render_template, make_response, jsonify
from opcua_client import read_node_val
from prefixs.prefixs import admin as prefix
from variables.admin import ADMIN, stop_reason

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route(prefix + "/<string:admin_link>")
def adminL(admin_link):
    try:
        response = ""

        if admin_link == "stop_reason" and read_node_val(ADMIN[admin_link]) != 0:
            value = int(math.floor(float(read_node_val(ADMIN[admin_link]))))
            response = jsonify({admin_link: stop_reason[value]})
        if response == "":
            response = jsonify({admin_link: read_node_val(ADMIN[admin_link])})

        return make_response(response, 200)
    except:
        return doesNotExist


@admin.route(prefix)
@admin.route(prefix+"/")
def doesNotExist():
    return render_template('admin.html', admin_links=ADMIN.keys())


@admin.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response