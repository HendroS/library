from . import blueprint
from controller import peminjamanController
from flask import request,g

@blueprint.route("/peminjaman", methods=['GET','POST'])
@blueprint.route("/peminjaman/<int:id>", methods=['GET',"DELETE"])
def peminjaman(id=None):
    method=request.method
    q=request.args.get('dikembalikan')
    # print(q)
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
        data= request.get_json()
        required=['petugas_id','user_id','tgl_kembali','books']
        not_present=[]
        for key in required:
            if key not in data.keys():
                not_present.append(key)
       

        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        # print(data["tgl_kembali"])
        if "keterangan" not in data.keys():
            data["keterangan"]=""
        
        result = peminjamanController.create(
            books=data["books"],
            keterangan=data["keterangan"],
            petugas_id=data["petugas_id"],
            tgl_kembali=data["tgl_kembali"],
            user_id=data["user_id"]    
        )
        return result

