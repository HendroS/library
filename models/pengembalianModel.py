import datetime
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey
from . import db


class Pengembalian(db.Model):
    pass
    __tablename__='pengembalian'
    pengembalian_id :Mapped[int]= mapped_column(db.Integer, primary_key=True)
    peminjaman_id:Mapped[int]= mapped_column(ForeignKey("peminjaman.peminjaman_id"), nullable=False,unique=True)
    tgl_kembali:Mapped[datetime.date] = mapped_column(db.Date,nullable=False,default=datetime.date.today())
    petugas_id:Mapped[str] = mapped_column(ForeignKey("users.user_id"),nullable=False)
    # petugas = relationship("User", uselist=False)

    def __repr__(self):
        return f'<Pengambalian {self.pengembalian_id} {self.peminjaman_id}>'