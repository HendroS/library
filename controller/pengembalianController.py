from models import Pengembalian,Book,DetailPinjaman
from . import db
import datetime

pengembalian=Pengembalian()

def getAll():
    try:
        result=pengembalian.query.all()
    except Exception as e:
        print(e)
        return {"message":"failed to get all data pengembalian"},500
    return {
        "daftar_pengembalian":[
            {
                "pengembalian_id":k.pengembalian_id,
                "peminjaman_id":k.peminjaman_id,
                "tgl_kembali":k.tgl_kembali,
                "tgl_pinjam":k.peminjaman.tgl_pinjam,
                "petugas_id":k.petugas_id,
                "petugas":k.petugas.username
            }
            for k in result]
    },200

def getById(id):
    result=pengembalian.query.filter_by(pengembalian_id=id).first_or_404()
    # pinjam= result.peminjaman.tgl_pinjam
    janji_kembali= result.peminjaman.tgl_kembali
    kembali= result.tgl_kembali
    keterangan=''
    if (kembali-janji_kembali).days>0:
        molor= (kembali-janji_kembali).days
        denda=0
        if molor<=7:
            denda= molor*1000
        else:
            denda = (7*1000)+ ((molor-7)*2000)
        keterangan=f'molor {(kembali-janji_kembali).days} hari.Denda Rp.{denda}'
    elif (kembali-janji_kembali).days==0:
        keterangan='tepat waktu banget'
    else:
        keterangan=f'aman. masih ada sisa waktu {(janji_kembali-kembali).days} hari lagi'
    return {
        'pengembalian_id':result.pengembalian_id,
        'peminjaman_id':result.peminjaman_id,
        'tgl_kembali':result.tgl_kembali,
        'petugas_id':result.petugas_id,
        'petugas':result.petugas.username,
        'keterangan':keterangan

    }

def delete(id):
    result=pengembalian.query.filter_by(pengembalian_id=id).first_or_404()
    try:
        db.session.delete(result)
        db.session.commit()
        janji_kembali= result.peminjaman.tgl_kembali
        kembali= result.tgl_kembali
        keterangan=''
        if (kembali-janji_kembali).days>0:
            molor= (kembali-janji_kembali).days
            denda=0
            if molor<=7:
                denda= molor*1000
            else:
                denda = (7*1000)+ ((molor-7)*2000)
            keterangan=f'molor {(kembali-janji_kembali).days} hari.Denda Rp.{denda}'
        elif (kembali-janji_kembali).days==0:
            keterangan='tepat waktu banget'
        else:
            keterangan=f'aman. masih ada sisa waktu {(janji_kembali-kembali).days} hari lagi'
    except Exception as e:
        print(e)
        return {"message":f"Failed to delete pengembalian id: {id}"},500
    return {"message":f"Pengembalian id: {id} deleted"},200

def create(peminjaman_id:int,petugas_id:int):
    try:
        pengembalian= Pengembalian(peminjaman_id=peminjaman_id,
                                   petugas_id=petugas_id
                                   )
        db.session.add(pengembalian)
        
        #get daftar buku dari detail pengembalian 
        details= DetailPinjaman().query.filter_by(peminjaman_id=peminjaman_id).all()
        for detail in details:
            
            #apakah benar satu per satu? atau biki array of book lalu dicommit bersama?
            book=Book.query.filter_by(detail.buku_id).first()
            #harusnya tidak perlu karena sudah pasti valid saat buat data peminjaman, kecuali database buku didelete
            if book==None:
                return {"message": f"buku id :{detail.buku_id} tidak ditemukan"},400

            book.stok=book.stok+detail.jumlah


        db.session.commit()
    except Exception as e:
        print(e)
        return {"message":"failed to create pengembalian data"},400
    return { "message":"succes create pengembalian",
            "data": {
                "pengembalian_id":pengembalian.pengembalian_id,
                "peminjaman_id":pengembalian.peminjaman_id,
                "petugas_id":pengembalian.petugas_id,
                "tgl_kembali":pengembalian.tgl_kembali,
            }

    }

def update(id:int,peminjaman_id:int,petugas_id:int):
    pengembalian=pengembalian.query.filter_by(pengembalian_id=id).first_or_404()
    try:
        if pengembalian.peminjaman_id != peminjaman_id:
            pengembalian.peminjaman_id = peminjaman_id
    except Exception as e:
        print(e)
        return {"message":f"update id: {id} failed"},400
    return {"message":f"update id: {id} success"}
        