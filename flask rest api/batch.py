from flask import Blueprint, render_template, make_response, jsonify
from prefixs.prefixs import batch as prefix
from variables.batchInfo import BATCH
from opcua_client import read_node_val

batch = Blueprint('batch', __name__, template_folder='templates')

@batch.route(prefix + "/<string:batch_info>")
def batch_in(batch_info):
    try:
        if batch_info == "all":
            return all()
        response = jsonify({batch_info: read_node_val(BATCH[batch_info])})
        return make_response(response, 200)
    except:
        return doesNotExist


@batch.route(prefix)
@batch.route(prefix+"/")
def doesNotExist():
    return render_template('batch.html', BATCHINFO=BATCH.keys())

def all():
    temp = BATCH.copy()

    for key in BATCH:
        temp[key] = read_node_val(temp[key])
    return make_response(jsonify(temp), 200)

@batch.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response

