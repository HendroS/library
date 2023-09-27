from . import blueprint
from controller import pengembalianController
from flask import request,g

@blueprint.route("/pengembalian", methods=['GET','POST'])
@blueprint.route("/pengembalian/<int:id>", methods=['GET'])
def pengembalian(id=None):
    method=request.method
    if method=="GET":
        if id==None:
            
            result = pengembalianController.getAll()
        else:
            result = pengembalianController.getById(id)
        return result
    if method == "POST":
        data=request.get_json()
        #check field
        result=pengembalianController.create(peminjaman_id=data["peminjaman_id"],
                                             petugas_id=data["petugas_id"]
                                             )
        return result
