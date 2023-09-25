from models import Peminjaman
from . import db

peminjaman = Peminjaman()

def getAll():
    result = peminjaman.query.all()
    # print(result)
    for x in result:
        print('nama petugas:',x.petugas.username)
        print('nama member:',x.member.username)
        # print('daftar buku:',[ b.judul for b in x.books.query.all])
        print(x.detail_pinjaman)

 
    return{"peminjaman":[
        {
        "peminjaman_id":peminjaman.user_id,
        "user_id":peminjaman.user_id,
        "petugas_id":peminjaman.petugas_id,
        "tgl_pinjam":peminjaman.tgl_pinjam,
        "tgl_kembali":peminjaman.tgl_kembali,
        "keterangan":peminjaman.keterangan,
        "daftar_pinjaman":[
            {
                "judul_buku":book.book.judul,
                "jumlah":book.jumlah
            }
            for book in peminjaman.detail_pinjaman
        ]
  
} for peminjaman in result
    ]
        
    }