from . import blueprint
from controller import bookController
from flask import request

@blueprint.route("/book", methods=['GET','POST'])
@blueprint.route("/book/<int:id>", methods=['GET',"DELETE","PUT"])
def book(id=None):
    method=request.method
    if method=="GET":
        if id==None:
            book=bookController.getAll()   
        else:
            book=bookController.getById(id)
        return book
    
    if method =="DELETE":
        result = bookController.deleteById(id)
        return result

    if method =="POST":
        data= request.get_json()
        required=['judul','tahun','jumlah_halaman','kategori_id','penulis']
        not_present=[]
        for key in required:
            if key not in data.keys():
                not_present.append(key)

        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result= bookController.create(
                                      authors_id=data["penulis"],
                                      judul=data["judul"],
                                      jumlah_halaman=data["jumlah_halaman"],
                                      tahun=data["tahun"],
                                      kategori_id=data["kategori_id"])
        return result

    if method =="PUT":
        data= request.get_json()
        required=['judul','tahun','jumlah_halaman','kategori_id','penulis']
        not_present=[]
        for key in required:
            if key not in data.keys():
                not_present.append(key)

        if len(not_present)>0:
            return {'error':'Bad Request',
                    'message':", ".join([f"{n} required" for n in not_present])+"."
                    },400
        result= bookController.update(id=id,
                                      authors_id=data["penulis"],
                                      judul=data["judul"],
                                      jumlah_halaman=data["jumlah_halaman"],
                                      tahun=data["tahun"],
                                      kategori_id=data["kategori_id"]
                                      )
        return result