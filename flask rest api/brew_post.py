from flask import Blueprint, make_response, jsonify, render_template, request
from flask_cors import cross_origin
from prefixs.prefixs import brew as prefix
from variables.brew import BREW, machine_speed
from variables.all import ALL
from opcua_client import write_node, read_node_val, convertVal

brew_post = Blueprint("brew_post", __name__)


@brew_post.route(prefix, methods=['POST'])
def brew_read():
    try:
        data = request.get_json()
        set_batch_id = convertVal(BREW.get("set_batch_id"), data.get('set_batch_id'))
        set_recipe = convertVal(BREW.get("set_recipe"), data.get('set_recipe'))
        set_quantity = convertVal(BREW.get("set_quantity"), data.get('set_quantity'))
        set_speed = convertVal(BREW.get("set_speed"), data.get('set_speed'))
    except:
        return make_response(
            'error in json body or values!\n Body should \nset_batch_id:float\nset_recipe:float\nset_quantity:float\nset_speed:float')

    if set_speed > machine_speed[set_recipe]:
        set_speed = machine_speed[set_recipe]
    elif set_speed <= 0:
        set_speed = 1

    brew_dict = {
        "set_batch_id": set_batch_id,
        "set_recipe": set_recipe,
        "set_quantity": set_quantity,
        "set_speed": set_speed,
    }

    for var, value in brew_dict.items():
        write_node(BREW.get(var), value)

    if read_node_val(ALL.get("current_state")) == 4:
        write_node(BREW.get("set_command"), 2)
        write_node(BREW.get("exec_command"), True)
    else:
        return make_response('reset')

    return make_response('The brew was successful!')

def test():
    print("done")


@brew_post.route(prefix + "/brew", methods=['POST'])
@cross_origin()
def brew_write():
    data = request.get_json()

    # code to handle the JSON-formatted data in the request
    print(data)
    response = make_response('The brew was successful!')
    return response


@brew_post.route(prefix)
@brew_post.route(prefix + "/")
def does_not_exist_brew_write():
    return render_template('write.html', items=BREW.keys(), subdomain=(prefix), all=False, example="set_speed")
