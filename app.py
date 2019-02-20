import csv
import json
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/", methods=['GET'])
def get():
    return 'Ok'

@app.route("/person/<string:net_id>", methods=['GET'])
def get_person(net_id):
    return(net_id)

@app.route("/training/<string:training_name>", methods=['GET'])
def get_trainings(training_name):
    return(training_name)

@app.route("/person_training/<string:net_id>/<string:training_name>", methods=['GET'])
def get_person_training(net_id, training_name):
    # use jsonify
    params = '{"' + net_id + '":"' + training_name + '"}'
    result = json.loads(params)
    return(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003)

# records = csv.reader(open("data/yTraining_Fall2018.csv", "rt"), delimiter=",")
# for row in records:
#     print(row)
