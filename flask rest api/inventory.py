from opcua_client import read_node_val
from flask import Blueprint, jsonify, make_response, render_template
from variables.ingredients import INGREDIENTS
from prefixs.prefixs import inventory as prefix

inventory = Blueprint('inventory', __name__, template_folder='templates')

@inventory.route(prefix + "/<string:ingredient>")
def ingredient(ingredient):
    if ingredient != "all":
        try:
            return make_response(jsonify({
                ingredient: read_node_val(INGREDIENTS[ingredient]),
            }), 200)
        except:
            return doesNotExist()
    else:
        return all()

@inventory.route(prefix)
@inventory.route(prefix+"/")
def doesNotExist():
    return render_template('inventory.html', ingredients=INGREDIENTS.keys())


def all():
    temp = INGREDIENTS.copy()

    for key in INGREDIENTS:
        temp[key] = read_node_val(temp[key])
    return make_response(jsonify(temp), 200)


@inventory.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response