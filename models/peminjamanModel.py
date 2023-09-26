import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from . import db


class Peminjaman(db.Model):
    __tablename__='peminjaman'
    peminjaman_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    petugas_id:Mapped[str] = mapped_column(ForeignKey("users.user_id"),nullable=False)
    user_id:Mapped[str] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    tgl_pinjam:Mapped[datetime.date] = mapped_column(db.Date,default=datetime.date.today(),nullable=False)
    tgl_kembali:Mapped[datetime.date] = mapped_column(db.Date,nullable=False)
    keterangan:Mapped[str] = mapped_column(db.String, nullable=True)
    member = relationship("User", back_populates="peminjaman_members",foreign_keys='Peminjaman.user_id')
    petugas = relationship("User", back_populates="petugas",foreign_keys='Peminjaman.petugas_id')
    detail_peminjaman=relationship('DetailPinjaman',back_populates="peminjaman")
    pengembalian = relationship("Pengembalian", uselist=False, backref="peminjaman")
   
    
    def __repr__(self):
        return f'<Peminjaman {self.peminjaman_id}>'