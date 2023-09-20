import datetime
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class Author(db.Model):
    __tablename__='penulis'
    penulis_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    nama:Mapped[str] = mapped_column(db.String, nullable=False)
    kewarganegaraan:Mapped[str] = mapped_column(db.String, nullable=False)
    tahun_kelahiran:Mapped[datetime.date] = mapped_column(db.Date,nullable=False)
    def __repr__(self):
        return f'<Penulis {self.nama}>'