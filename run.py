from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return  jsonify({'hello': 'world'})


app.run(host='0.0.0.0',port='5000')