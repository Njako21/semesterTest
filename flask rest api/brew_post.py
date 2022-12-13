from flask import Blueprint, make_response, jsonify, render_template, request
from flask_cors import cross_origin
from prefixs.prefixs import brew_post as prefix
from variables.brew import BREW
from opcua_client import read_node, write_node

brew_post = Blueprint("brew_post", __name__)


@brew_post.route(prefix + "/brew", methods=['POST'])
@cross_origin()
def brew_write():
    write_node(BREW['set_batch_id'], "float", 300)
    write_node(BREW['set_recipe'], "float", 0)
    write_node(BREW['set_quantity'], "float", 300)
    write_node(BREW['set_speed'], "float", 300) #speed
    write_node(BREW['set_command'], "int32", 2)
    write_node(BREW['exec_command'], "bool", True)


    data = request.get_json()
    # code to handle the JSON-formatted data in the request
    print(data)
    response = make_response('The brew was successful!')
    return response


@brew_post.route(prefix)
@brew_post.route(prefix + "/")
def does_not_exist_brew_write():
    return render_template('write.html', items=BREW.keys(), subdomain=(prefix), all=True, example="set_speed")
