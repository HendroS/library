from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

author_book= db.Table('penulis_buku',
    db.Column('penulis_id', db.Integer, db.ForeignKey('penulis.penulis_id'), primary_key=True),
    db.Column('buku_id', db.Integer, db.ForeignKey('buku.buku_id'), primary_key=True)
)

# detail_pinjaman= db.Table('detail_pinjamanan',
#     db.Column('peminjaman_id', db.Integer, db.ForeignKey('peminjaman.peminjaman_id'), primary_key=True),
#     db.Column('buku_id', db.Integer, db.ForeignKey('buku.buku_id'), primary_key=True),
#     db.Column('jumlah',db.Integer,nullable=False)
#     )


from .authorModel import Author
from .categoryModel import Category
from .bookModel import Book
from .userModel import User
from .peminjamanModel import Peminjaman
from .detailPinjamanModel import DetailPinjaman
# from .pengembalianModel import Pengembalian



