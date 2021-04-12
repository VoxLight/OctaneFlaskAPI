import flask
from flask import request, jsonify, abort
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals
app = flask.Flask(__name__)
app.config["DEBUG"] = True


data = [
    {"id":0, "name":"number1", "bool":True},
    {"id":1, "name":"number2", "bool":False},
    {"id":2, "name":"number3", "bool":True},
    {"id":3, "name":"number4", "bool":False},
    {"id":4, "name":"number5", "bool":True},
    {"id":5, "name":"number6", "bool":False},
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>API</h1><p>use /api/v1/data</p>"

@app.route('/api/v1/data/all', methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/api/v1/data', methods=['GET'])
def api_id():
    if 'id' in request.args:
        for entry in data:
            if entry["id"] == int(request.args["id"]):
                return jsonify(entry)
            
    return abort(404) # Returns 404 if no id is given or if id is not found

@app.route('/api/test', methods=['GET', 'POST'])
def test_request():
    print(request.args)
    print(request.form)
    print(request.files)
    print(request.json)
    return "Yee"
    

app.run()