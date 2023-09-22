from sqlalchemy.orm import Mapped, mapped_column
from . import db

class User(db.Model):
    __tablename__='users'
    user_id:Mapped[int]= mapped_column(db.Integer, primary_key=True)
    username:Mapped[str] = mapped_column(db.String, nullable=False,unique=True)
    password:Mapped[str] = mapped_column(db.String(60), nullable=False)
    isadmin: Mapped[bool] = mapped_column(db.Boolean,nullable=False,default=True)

    def __repr__(self):
        return f'<Book {self.username}>'