from models import Peminjaman, Book, DetailPinjaman
from . import db

peminjaman = Peminjaman()

def getAll():
    result = peminjaman.query.all()
    # for x in result:
    #     print('nama petugas:',x.petugas.username)
    #     print('nama member:',x.member.username)
    #     # print('daftar buku:',[ b.judul for b in x.books.query.all])
    #     print(x.detail_peminjaman)
    #     print(x.petugas.username)

 
    return {"peminjaman":[
        {
        "peminjaman_id":peminjaman.peminjaman_id,
        "user_id":peminjaman.user_id,
        "petugas_id":peminjaman.petugas_id,
        "petugas":peminjaman.petugas.username,
        "member":peminjaman.member.username,
        "tgl_pinjam":peminjaman.tgl_pinjam,
        "tgl_kembali":peminjaman.tgl_kembali,
        "keterangan":peminjaman.keterangan,
        "daftar_pinjaman":[
            {
                "judul_buku":book.book.judul,
                "jumlah":book.jumlah
            }
            for book in peminjaman.detail_peminjaman
        ]
  
} for peminjaman in result
    ]     
    }

def getById(id):
    result = peminjaman.query.filter_by(peminjaman_id=id).first_or_404()
    # print(result.pengembalian)
    return{"peminjaman":{
        "peminjaman_id":result.peminjaman_id,
        "user_id":result.user_id,
        "petugas_id":result.petugas_id,
        "petugas":result.petugas.username,
        "member":result.member.username,
        "tgl_pinjam":result.tgl_pinjam,
        "tgl_kembali":result.tgl_kembali,
        "keterangan":result.keterangan,
        "status":'belum dikembalikan' if result.pengembalian == None else "sudah dikembalikan",
        "daftar_pinjaman":[
            {
                "judul_buku":book.book.judul,
                "jumlah":book.jumlah
            }
            for book in result.detail_peminjaman
        ]
        }}

def deleteById(id):
    result = peminjaman.query.filter_by(peminjaman_id=id).first_or_404()

    try:
        result.detail_peminjaman=[]
        db.session.delete(result)
        db.session.commit()
    except Exception as e:
        print(e)
        return {'message':f'error while delete peminjaman id: {id}'},400
    return {"message":f'delete peminjaman id: {result.peminjaman_id} success'},200

def create(petugas_id,user_id,tgl_kembali,keterangan,books):
    try:
        peminjaman=Peminjaman(petugas_id=petugas_id,
                              user_id=user_id,
                              tgl_kembali=tgl_kembali,
                              keterangan=keterangan
                              )
        if len(books)<1:
            return {"message":'buku pinjaman tidak boleh kosong'},400
        db.session.add(peminjaman)
        for book in books:
            if "buku_id" not in book.keys() :
                return {"message":'buku_id tidak boleh kosong'},400
            if "jumlah" not in book.keys():
                return {"message":'jumlah dari buku tidak boleh kosong'},400
            if book["jumlah"] <1:
                return {"message":'jumlah dari buku minimal 1'},400
            b=Book().query.filter_by(buku_id=book["buku_id"]).first()
            if b==None:
                return {"message":f"book_id tidak terdaftar di database"}
            # print(b)
            detail=DetailPinjaman(peminjaman_id=peminjaman.peminjaman_id,
                                  buku_id=book["buku_id"],
                                  jumlah=book["jumlah"])
            peminjaman.detail_peminjaman.append(detail)
            print(detail.book)
            

        print(peminjaman.detail_peminjaman)

        db.session.commit()

    except Exception as e:
        print(e)
        return {"message":f"insert new peminjaman failed"},500
    return {"message":f"add new peminjaman with id : {peminjaman.peminjaman_id} success",
            "peminjaman":{
        "peminjaman_id":peminjaman.peminjaman_id,
        # "user_id":peminjaman.user_id,
        # "petugas_id":peminjaman.petugas_id,
        "petugas":peminjaman.petugas.username,
        "member":peminjaman.member.username,
        "tgl_pinjam":peminjaman.tgl_pinjam,
        "tgl_kembali":peminjaman.tgl_kembali,
        "keterangan":peminjaman.keterangan,
        "daftar_pinjaman":[
            {
                "judul_buku":book.book.judul,
                "jumlah":book.jumlah
            }
            for book in peminjaman.detail_peminjaman
        ]
        }},200
        
def update(id,petugas_id,user_id,tgl_kembali,keterangan,books):
    #apakah perlu
    pass
