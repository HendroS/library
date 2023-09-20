from . import blueprint
from controller import categoryController

@blueprint.route("/category", methods=['GET'])
def hello_world():
    categories= categoryController.getAll()
    return categories