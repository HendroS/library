from sqlalchemy.orm import Mapped, mapped_column,relationship
from . import db

class User(db.Model):
    __tablename__='users'
    user_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    username:Mapped[str] = mapped_column(db.String, nullable=False,unique=True)
    password:Mapped[str] = mapped_column(db.String(60), nullable=False)
    isadmin: Mapped[bool] = mapped_column(db.Boolean,nullable=False,default=True)
    peminjaman_members= relationship('Peminjaman',back_populates='member',foreign_keys='Peminjaman.user_id')
    petugas=relationship('Peminjaman',back_populates='petugas',foreign_keys='Peminjaman.petugas_id')
    # peminjaman_petugas= db.relationship('Peminjaman',back_populates='petugas',foreign_keys='peminjaman.petugas_id')
    
    pengembalian_petugas= db.relationship('Pengembalian',backref='petugas',lazy=True)

    def __repr__(self):
        return f'<user {self.username}>'