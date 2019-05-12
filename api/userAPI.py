from flask import Flask, Blueprint, request, Response
from .db import MysqlDatabase
from api.auth import check_auth, authenticate, requires_auth

user_api = Blueprint("user_api", __name__)

db = MysqlDatabase('u615qyjzybll9lrm.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', 'znrv09cif9r6878k', 'besy5nu30n3u1hrh', 'ffl0zhvdujs4a0wc')

@user_api.route('/users')
@requires_auth
def checkUser():
    auth = request.authorization
    print(auth)
    select = "SELECT id, pseudo, mail FROM user where pseudo like '%s'" % auth.username
    result = db.execute(query=select)
    return result