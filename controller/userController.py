from sqlalchemy import text
from models import User
from . import db,Auth
import bcrypt

users=User()


def getById(id:int):
    result=users.query.filter_by(user_id=id).first_or_404()
    return {
        "user_id":result.user_id,
        "username":result.username,
        "password":result.password,
        "role":'admin' if result.isadmin == True else 'user'
}

def getAll():
    result = users.query.all()
    
    return{"users":[
        {
        "user_id":user.user_id,
        "username":user.username,
        "password":user.password,
        "role":'admin' if user.isadmin == True else 'user'
} for user in result
    ]
        
    }
def create(username:str,password:str):
    user= users.query.filter_by(username=username).first()
    if user!=None:
        return {'message':f'username {username} already exist'},400

    try:
        salt= bcrypt.gensalt()
        password= password.encode('utf-8')
        hashed=bcrypt.hashpw(password,salt)
        hashed=hashed.decode('utf-8')
        user=User(username=username,password=hashed)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return {
            'message':'create user failed'
        },400
    return {
        "user_id":user.user_id,
        "username":user.username,
        "password":user.password,
        "role":'admin' if user.isadmin == True else 'user'
    }

def deleteById(id:int):
    user=users.query.filter_by(user_id=id).first_or_404()
    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return{
            "message":f"delete user id : {id} failed"
        },400
    return {"message":f"delete user id: {id} success"
    },200

def update(id:int,username:str,password:str):
    
    try:
        user=users.query.filter_by(user_id=id).first_or_404()
        if user.username!=username:
            count_user=users.query.filter_by(username=username).count()
            if count_user>0:
                return {'message':f'username \'{username}\' already exist!'},400
            
            user.username=username

        salt= bcrypt.gensalt()
        password= password.encode('utf-8')
        hashed=bcrypt.hashpw(password,salt)
        hashed=hashed.decode('utf-8')
        user.password=hashed
        db.session.commit()
    except Exception as e:
        print(e)
        return {
            "message":"update failed"
        },400
    return {
        "message":f'update user id: {id} success'
    },200
        

def topUser(numbers=5):
    q=text(f"SELECT u.username, count(p.peminjaman_id) jumlah_peminjaman FROM peminjaman p\
           JOIN users u on u.user_id = p.user_id\
           GROUP BY u.username\
           ORDER BY jumlah_peminjaman DESC\
           LIMIT {numbers}")
    result= db.engine.connect().execute(q).mappings().all()
    r=[dict(x) for x in result]
    

    return {f"top_{numbers}_frequents":r}    


