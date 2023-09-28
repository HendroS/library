from helpers.utils import checkField
from . import blueprint
from controller import userController,Auth
from flask import abort, request,g

@blueprint.route("/user", methods=['GET','POST'])
@blueprint.route("/user/<int:id>", methods=['GET',"DELETE","PUT"])
def user(id=None):
    method=request.method
    g.auth.setAllowed(['member','admin'])

    if method=="PUT":
        data=request.get_json()
        not_present=checkField(['username','password'],data)
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        if data["username"]!=g.auth.user['username']:
            abort(401,"Only account owner can update")
        result =userController.update(id=id,username=data["username"],password=data["password"])
        return result
    
    g.auth.setAllowed(['admin'])
    if method=='GET':
        if id==None:
            user=userController.getAll()
        else:
            user=userController.getById(id)
        return user
    if method=='POST':
        data=request.get_json()
        not_present=checkField(['username','password'],data)
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result = userController.create(username=data['username'],
                                       password=data['password']
                                       )
        return result
    if method=='DELETE':
        result=userController.deleteById(id)
        return "result" 
   