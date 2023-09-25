from functools import wraps
from flask import Blueprint,g
from controller import Auth

blueprint = Blueprint('my_blueprint', __name__)


@blueprint.before_request
def authentication():
    g.auth= Auth()

from . import category
from . import author
from . import book
from . import user
from . import peminjaman

@blueprint.errorhandler(401)
def custom_401(error):
    return{'message':'unauthorized'},401

