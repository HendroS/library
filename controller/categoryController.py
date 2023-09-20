from models import Category
from . import db

categories= Category()

def getById(id:int):
    result=categories.query.filter_by(kategori_id=id).first()

    return {
        "deskripsi_id":result.kategori_id,
        "nama":result.nama,
        "deskripsi":result.deskripsi
    }


def getAll():
    result = categories.query.all()
    return {
        "categories": [c.nama for c in result]
    }

def deleteById(id):
    category=categories.query.filter_by(kategori_id=id).first()
    db.session.delete(category)
    db.session.commit()
    return {
            "message":'Delete success'
        }
