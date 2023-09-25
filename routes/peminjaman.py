from . import blueprint
from controller import peminjamanController
from flask import request,g

@blueprint.route("/peminjaman", methods=['GET'])
def peminjaman():
    p=peminjamanController.getAll()
    return p
