from models import Category
from . import db

categories= Category()

def getById(id:int):
    result=categories.query.filter_by(kategori_id=id).first_or_404()
    
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
    try:
        category=categories.query.filter_by(kategori_id=id).first()
        db.session.delete(category)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"message":"delete failed"},400
    return {
            "message":'Delete success'
        }

def create(nama,deskripsi):
        try:
            category = Category(
                            nama=nama,
                            deskripsi=deskripsi
                            )
            db.session.add(category)
            db.session.commit()
            
        except Exception as e:
            print(e.orig)
            return {
                # "error":str(e),
                "message":"insert failed"},400
        
        return {"message":"insert success"},200

def update(id,nama,deskripsi):
    category=categories.query.filter_by(kategori_id=id).first_or_404()
    try:
        category.nama=nama
        category.deskripsi= deskripsi
        db.session.commit()
    except Exception as e:
        print(e.orig)
        return {
                "message":"update failed"},400
        
    return {"message":f"update author id: {category.kategori_id} success"},200