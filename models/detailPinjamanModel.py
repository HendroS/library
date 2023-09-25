import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class DetailPinjaman(db.Model):
    __tablename__='detail_pinjaman'
    peminjaman_id: Mapped[int] = mapped_column(ForeignKey("peminjaman.peminjaman_id"),primary_key=True)
    buku_id:Mapped[int]= mapped_column(ForeignKey("buku.buku_id"),primary_key=True)
    jumlah:Mapped[int]= mapped_column('jumlah',db.Integer,nullable=False)
    book=db.relationship('Book')
    peminjaman=db.relationship('Peminjaman')


    def __repr__(self) -> str:
        return f"<detail book: {self.buku_id} jumlah :{self.jumlah}>"
