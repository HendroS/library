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
from . import pengembalian

@blueprint.errorhandler(401)
def custom_401(error):
    # print(error.description)
    return{'message':'unauthorized',
           'description':error.description},401

