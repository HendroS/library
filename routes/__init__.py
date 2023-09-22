from flask import Blueprint

blueprint = Blueprint('my_blueprint', __name__)

from . import category
from . import author
from . import book
from . import user