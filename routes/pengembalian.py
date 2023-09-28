from helpers.utils import checkField
from . import blueprint
from controller import pengembalianController
from flask import request,g

@blueprint.route("/pengembalian", methods=['GET','POST'])
@blueprint.route("/pengembalian/<int:id>", methods=['GET'])
def pengembalian(id=None):
    method=request.method
    g.auth.setAllowed(['admin'])
    if method=="GET":
        if id==None:      
            result = pengembalianController.getAll()
        else:
            result = pengembalianController.getById(id)
        return result
    if method == "POST":
        data=request.get_json()
        #check field
        not_present=checkField(['peminjaman_id'],data)
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result=pengembalianController.create(peminjaman_id=data["peminjaman_id"],
                                             petugas_id=g.auth.user['id']
                                             )
        return result
