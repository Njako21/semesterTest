from flask_cors import cross_origin

from opcua_client import write_node, read_node
from flask import Blueprint, jsonify, make_response, request, Response
from variables.brew import BREW
from prefixs.prefixs import write as prefix

writer = Blueprint('write', __name__, template_folder='templates')

@writer.route(prefix + "/<string:string>", methods=['POST'])
@cross_origin()
def write(string):


    try:
        data = request.get_json()
        node = BREW.get(string)

        value = data.get('value')

        write_node(node, value)
        if string == "set_command":
            write_node(BREW.get("exec_command"), True)
        print(string)
        response = Response({
            'sucess': 'yes',
        })
    except:
        print("cant find var:|"+string+"|")
        response = Response({
            'sucess': 'no',
        })
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8000'
    return response


@writer.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response