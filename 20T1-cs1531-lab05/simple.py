from flask import Flask, request
from json import dumps
APP = Flask(__name__)

data = {}
data['name'] = []

def getdata():
    global data
    return data

@APP.route("/name/add", methods = ['POST'])
def add_name():
    data = getdata()
    add = request.get_json('add')
    data['name'].append(add)

@APP.route("/names", methods = ['GET'])
def get_name():
    data = getdata()
    return dumps({
        'name' : request.args.get(data['name'])
    })

@APP.route("/name/remove", methods = ['DELETE'])
def delete_name():
    data = getdata()
    remove = request.get_json('remove')
    data['name'].remove(remove)


if __name__ == "__main__":
    APP.run()