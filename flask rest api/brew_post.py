from flask import Blueprint, make_response, jsonify, render_template, request
from flask_cors import cross_origin
from prefixs.prefixs import brew_post as prefix
from variables.brew import BREW

brew_post = Blueprint("brew_post", __name__)


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
    return render_template('write.html', items=BREW.keys(), subdomain=(prefix), all=True, example="set_speed")
