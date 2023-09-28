from helpers.utils import checkField
from . import blueprint
from controller import authorController,Auth
from flask import request,g

@blueprint.route("/author", methods=['GET','POST'])
@blueprint.route("/author/<int:id>", methods=['GET',"DELETE","PUT"])
def author(id=None):
    method=request.method
    
    g.auth.setAllowed(['admin','member'])
    if method=="GET":
        if id==None:
            author=authorController.getAll()
        else:
            author=authorController.getById(id)
        return author
    
    g.auth.setAllowed['admin']
    if method=="DELETE":
        result= authorController.deleteById(id)
        return result
    
    if method=="POST":
        data= request.get_json()
        required=['nama','kewarganegaraan','tahun_kelahiran']
        not_present=checkField(data=data,required=required)

        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result = authorController.create(
            nama=data['nama'],
            kewarganegaraan=data['kewarganegaraan'],
            tahun_kelahiran=data['tahun_kelahiran']
            )
        return result
    
    if method == "PUT":
        data= request.get_json()
        required=['nama','kewarganegaraan','tahun_kelahiran']
        not_present=checkField(data=data,required=required)

        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400

        result = authorController.update(id=id,
                                        nama=data['nama'],
                                        kewarganegaraan=data['kewarganegaraan'],
                                        tahun_kelahiran=data['tahun_kelahiran'])
        return {'message':f'update author id:{id} success'}
        