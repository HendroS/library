from models import Book
from models import Author
from . import db

books=Book()

def getById(id:int):
    try:
        result=books.query.filter_by(buku_id=id).first()
    except Exception as e:
        print(e)
        return {'message':f'error while get book id: {id}'}
    return {
        "buku_id":result.buku_id,
        "judul":result.judul,
        "jumlah_halaman":result.jumlah_halaman,
        "tahun":result.tahun,
        "kategori":result.category.nama,
        "stok":result.stok,
        "authors":[c.nama for c in result.authors]
    },200
def getAll():
    try:
        result=books.query.all()
    except Exception as e:
        print(e)
        return {'message':'error while get books'}
    return {"books":[{
        "buku_id":book.buku_id,
        "judul":book.judul,
        "jumlah_halaman":book.jumlah_halaman,
        "tahun":book.tahun,
        "stok":book.stok,
        "kategori":book.category.nama,
        "authors":[c.nama for c in book.authors]} for book in result]}

def deleteById(id:int):
    try:
        book=books.query.filter_by(buku_id=id).first()
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print(e)
        return {'message':f'error while delete book id: {id}'}
    return {
        "message":f'delete book delete book id: {id} success ',
    },200

def create(judul:str,jumlah_halaman:int,tahun:str,kategori_id:int,authors_id:[int],stok:int=1):
    if len(authors_id)<1:
        return {'message':f'required at least 1 author for a book'},400
    if stok<1:
        return {'message':f'required at least 1 stock for a book'},400
    try:
        book= Book(judul=judul,
                   jumlah_halaman=jumlah_halaman,
                   tahun=tahun,
                   kategori_id=kategori_id,
                   stok=stok
                   )
        db.session.add(book)
        for id in authors_id:
            a= Author().query.filter_by(penulis_id=id).first()
            if a== None:
                return {"message":f'author id : {id} not found'},400
            book.authors.append(a)
    except Exception as e:
        print(e)
        return {'message':f'error while create new book'},400
    return {"message":"insert new book success",
                "book":{
                    "id":book.buku_id,
                    "judul":book.judul,
                    "authors":[author.nama for author in book.authors]
                    }
            },200

def update(id,judul:str,jumlah_halaman:int,tahun:str,kategori_id:int,authors_id:[int],stok:int):
    book=books.query.filter_by(buku_id=id).first_or_404()
    if len(authors_id)<1:
        return {'message':f'required at least 1 author for a book'},400
    try:
        book.judul=judul
        book.jumlah_halaman=jumlah_halaman
        book.kategori_id=kategori_id
        book.tahun=tahun
        book.stok=stok
        book.authors=[]
        for penulis_id in authors_id:
            author= Author().query.filter_by(penulis_id=penulis_id).first()
            if author== None:
                return {"message":f'author with id: {id} is not found'},400
            book.authors.append(author)
        db.session.commit()
    except Exception as e:
        print(e)
        return {'message':f'error while update book with id: {id}'},400
    return {
        "message":f'Book with id:{id} updated'
    },200