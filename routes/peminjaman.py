from helpers.utils import checkField
from . import blueprint
from controller import peminjamanController
from flask import request,g

@blueprint.route("/peminjaman", methods=['GET','POST'])
@blueprint.route("/peminjaman/<int:id>", methods=['GET',"DELETE"])
def peminjaman(id=None):
    method=request.method
    q=request.args.get('dikembalikan')
    method=request.method

    g.auth.setAllowed(['admin'])

    if method=="GET":
        if id==None:
            print(q)
            result=peminjamanController.getAll(dikembalikan=q)
        else:
            result=peminjamanController.getById(id)
        return result
    if method=="DELETE":
        result= peminjamanController.deleteById(id)
        return result
    if method=="POST":
        # print(g.auth.user['id'])
        data= request.get_json()
        required=['user_id','tgl_kembali','books']
        not_present=checkField(required,data)
        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        if "keterangan" not in data.keys():
            data["keterangan"]=""
        
        result = peminjamanController.create(
            books=data["books"],
            keterangan=data["keterangan"],
            petugas_id=g.auth.user['id'],
            tgl_kembali=data["tgl_kembali"],
            user_id=data["user_id"]    
        )
        return result

