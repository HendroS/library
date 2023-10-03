from helpers.utils import checkField
from . import blueprint
from controller import bookController,userController
from flask import abort, request,g

@blueprint.route("/report/favoritebook", methods=['GET','POST'])
def favorites_book():
    result = bookController.getFavorites()
    return result

@blueprint.route("/report/topuser", methods=['GET','POST'])
def topUser():
    q=request.args.get('numbers')
    if q == None:
        q=5
    result = userController.topUser(q)
    return result