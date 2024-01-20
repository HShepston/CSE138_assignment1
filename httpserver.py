from flask import Flask, json, request

app = Flask(__name__)

@app.route("/ping", methods=['GET', 'PUT'])
def ping():
    if request.method == 'GET':
        rv = {
            "message": "I'm alive!!",
            "status": 200
        }
    else:
        rv = {
            "message": "Method Not Allowed",
            "status": 405
        }
    return json.dumps(rv)

@app.route("/ping/<name>", methods=['GET', 'PUT'])
def pingn(name):
    if request.method == 'PUT':
        rv = {
            "message": f"I'm alive, {name}!!",
            "status": 200
        }
    else:
        rv = {
            "message": "Method Not Allowed",
            "status": 405
        }
    return json.dumps(rv)

@app.route("/echo", methods=['GET', 'PUT'])
def echo():
    if request.method == 'GET':
        rv = {
            "message":"Get Message Received",
            "status": 200
        }
    else:
        rv = {
            "message": f"Flask.data",
            "status": 200
        }
    return json.dumps(rv)

if __name__ == '__main__':
    app.run(port=8085)
