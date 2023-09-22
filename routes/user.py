from . import blueprint
from controller import userController
from flask import request

@blueprint.route("/user", methods=['GET','POST'])
@blueprint.route("/user/<int:id>", methods=['GET',"DELETE","PUT"])
def user(id=None):
    method=request.method
    print(method)

    if method=='GET':
        if id==None:
            user=userController.getAll()
        else:
            print('userroute')
            user=userController.getById(id)
        return user
    if method=='POST':
        data=request.get_json()
        result = userController.create(username=data['username'],
                                       password=data['password']
                                       )
        return result
    if method=='DELETE':
        result=userController.deleteById(id)
        return "result"
    
    if method=="PUT":
        data=request.get_json()
        result =userController.update(id=id,username=data["username"],password=data["password"])
        return result