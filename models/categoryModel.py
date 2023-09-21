# from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .import db

class Category(db.Model):
    __tablename__='kategori'
    kategori_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    nama:Mapped[str] = mapped_column(db.String, nullable=False)
    deskripsi:Mapped[str] = mapped_column(db.String,nullable=False)
    books= db.relationship('Book',backref='category',lazy=True)