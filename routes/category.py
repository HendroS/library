from helpers.utils import checkField
from . import blueprint
from controller import categoryController,Auth
from flask import request,g

@blueprint.route("/category", methods=['GET','POST'])
@blueprint.route("/category/<int:id>", methods=['GET',"DELETE","PUT"])
def category(id=None):
    method=request.method
    g.auth.setAllowed(['admin','member'])
    if method=="GET":
        if id==None:
            category=categoryController.getAll()
        else:
            category=categoryController.getById(id)
        return category
    
    g.auth.setAllowed(['admin'])

    if method=="DELETE":
        result= categoryController.deleteById(id)
        return result
    if method == "PUT":
        data= request.get_json()
        not_present=checkField(data=data,required=['nama','deskripsi'])
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result = categoryController.update(id,data['nama'],data['deskripsi'])
        return result
    if method=="POST":
        data= request.get_json()
        not_present=checkField(data=data,required=['nama','deskripsi'])
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        
        result = categoryController.create(nama=data['nama'],deskripsi=data['deskripsi'])
        return result
        

