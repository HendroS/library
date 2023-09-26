import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from . import db,author_book

class Book(db.Model):
    __tablename__='buku'
    buku_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    judul:Mapped[str] = mapped_column(db.String, nullable=False)
    jumlah_halaman:Mapped[str] = mapped_column(db.String, nullable=False)
    tahun:Mapped[datetime.date] = mapped_column(db.Date,nullable=False)
    kategori_id: Mapped[int] = mapped_column(ForeignKey("kategori.kategori_id"))
    
    authors = db.relationship('Author', secondary=author_book, lazy='subquery',
        backref=db.backref('books', lazy=True))
    detail_pinjaman= db.relationship('DetailPinjaman',backref='book',lazy=True)
    # detail_pinjaman=relationship('DetailPinjaman',back_populates="book")
    
    # peminjaman = db.relationship('Peminjaman', secondary=detail_pinjaman, lazy='subquery',
    #     backref=db.backref('books', lazy=True))
    def __repr__(self):
        return f'<Book {self.judul}>'