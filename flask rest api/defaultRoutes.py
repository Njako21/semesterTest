from flask import Blueprint, render_template

from prefixs.prefixs import api

defRoutes = Blueprint('defRoutes', __name__, template_folder='templates')

@defRoutes.route("/")
@defRoutes.route(api)
@defRoutes.route(api+"/")
def doesNotExist():
    return render_template('api.html')

@defRoutes.route(api+"/howTo")
def howTo():
    return render_template('howTo.html')