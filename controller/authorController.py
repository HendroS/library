from models import Author
from . import db

authors=Author()

def getById(id:int):
    result=authors.query.filter_by(penulis_id=id).first()
    return {
        "penulis_id":result.kategori_id,
        "nama":result.nama,
        "kewarganegaraan":result.deskripsi,
        "tahun_kelahiran":result.tahun_kelahiran
    }


def getAll():
    result = authors.query.all()
    return {
        "authors": [a.nama for a in result]
    }

def create(nama:str,kewarganegaraan,tahun_kelahiran):
    try:
            author = Author(
                            nama=nama,
                            kewarganegaraan=kewarganegaraan,
                            tahun_kelahiran=tahun_kelahiran
                            )
            db.session.add(author)
            db.session.commit()
            
    except Exception as e:
            print(e)
            return {
                # "error":str(e),
                "message":"insert failed"},400
        
    return {"message":"insert success"},200



def update(id,nama:str,kewarganegaraan:str,tahun_kelahiran:str):
    try:
        author=authors.query.filter_by(penulis_id=id).first()
        author.nama=nama
        author.kewarganegaraan=kewarganegaraan
        author.tahun_kelahiran=tahun_kelahiran
        db.session.commit()
    except Exception as e:
            print(e)
            return {
                # "error":str(e),
                "message":"update failed"},400
    
    return {"message":f"insert author id :{author.penulis_id} success"},200

def deleteById(id:int):
    try:
        author=authors.query.filter_by(penulis_id=id).first()
        db.session.delete(author)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"message":"delete failed"},400
    
    return {"message":"delete success"},200
      