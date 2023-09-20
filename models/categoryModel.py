# from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from models import db

class Category(db.Model):
    __tablename__='kategori'
    kategori_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    nama:Mapped[str] = mapped_column(db.String, nullable=False)
    deskripsi:Mapped[str] = mapped_column(db.String,nullable=False)