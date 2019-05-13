from flask import Flask, Blueprint, request, Response, jsonify
import json
from functools import wraps
from .db import MysqlDatabase
from api.hash import verify

db = MysqlDatabase('u615qyjzybll9lrm.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', 'znrv09cif9r6878k', 'besy5nu30n3u1hrh', 'ffl0zhvdujs4a0wc')

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """

    select = "SELECT * FROM user where pseudo like '%s'" % username
    result = db.execute(query=select)
    users = json.loads(result)
    
    if(len(users) > 0):
        items = password.split(":")
        if len(items) > 0 and items[0] == "bio":
            return users[0]['biometry'] == items[1]
        else:
            return verify(users[0]['password'], password)
    else:
        return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated