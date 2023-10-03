from helpers.utils import checkField
from . import blueprint
from controller import bookController,Auth
from flask import render_template, request,g

@blueprint.route("/book", methods=['GET','POST'])
@blueprint.route("/book/<int:id>", methods=['GET',"DELETE","PUT"])
def book(id=None):
    method=request.method
    g.auth.setAllowed(['admin','member'])
    if method=="GET":
        if id==None:
            book=bookController.getAll()   
            
            # for b in book["books"]:
            #     print(b)
        else:
            book=bookController.getById(id)
        return book
        # return render_template('book.html',data=book["books"])
    
    g.auth.setAllowed(['admin'])
    if method =="DELETE":
        result = bookController.deleteById(id)
        return result

    if method =="POST":
        data= request.get_json()
        required=['judul','tahun','jumlah_halaman','kategori_id','penulis']
        not_present=checkField(data=data,required=required)

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
        not_present=checkField(data=data,required=required)

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