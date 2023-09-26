import bcrypt
from flask import abort, request
from models import User


class Auth():

    def __init__(self,roles:[str]=[]) -> None:
        self.user=None
        self.authorized=False
        self.__isAuth()
        self.setAuthorization(roles)

    def __isAuth(self)->None:
        credential=request.authorization
        if credential != None and credential.type=='basic':
            username=credential.parameters['username']
            password=credential.parameters['password']
            user=User().query.filter_by(username=username).first()
            if user!=None:
                isMatch=bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8'))
                if isMatch==True:
                    self.user={"username":user.username,
                               "role":"admin" if user.isadmin ==True else "member"}
            #     else:
            #         print("wrong pass")
            # else:print ('not registered')
    
    def setAuthorization(self,roles:[str]=[]):
        if self.user!=None:
            if len(roles)==0 or self.user["role"] in roles:
                self.authorized=True
            else:
                self.authorized=False
                abort(401)
        elif len(roles)==0:
            self.authorized=True
        else:
            abort(401)





                
    




# def isAdmin():
#     credential=request.authorization
#     if credential == None or len(str(credential).split(" "))!=2:
#         pass

#     credential=str(credential).split(" ")
#     auth_type=credential[0]
#     username_pass=credential[1]
#     print(username_pass)

    # password ='1234'
    # password= password.encode('utf-8')
    # print(password)
    # salt= bcrypt.gensalt()

    # hashed=bcrypt.hashpw(password,salt)