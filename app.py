import csv
import json
from flask import Flask, json

# I need to verify the expected output of these functions and see that the actual output matches.
# I could also build a few test cases that get run when a new record is uploaded.

app = Flask(__name__)
app.config.from_object(__name__)

# name of file containing most current yTraining records
# please make sure that this file exists in the "Data" folder within this application.
records_file = "yTraining_Fall2018.csv"

@app.route("/", methods=['GET'])
def get():
    return 'Ok'

# return all trainings completed by a person
@app.route("/person/<string:net_id>", methods=['GET'])
def get_person(net_id):
    rows = []
    records = csv.reader(open("data/"+records_file, "rt"), delimiter=",")
    for row in records:
        # thus far, net IDs are stored all uppercase. Case-insensitive search would be better.
        if net_id.upper() in row[0]:
            print(row)
            rows.append(row)
    return json.dumps(rows)

# return all users who have completed a training
@app.route("/training/<string:training_name>", methods=['GET'])
def get_trainings(training_name):
    rows = []
    records = csv.reader(open("data/"+records_file, "rt"), delimiter=",")
    for row in records:
        if training_name in row[1]:
            print(row)
            rows.append(row)
    return json.dumps(rows)

# return 1 if a specified user has completed a specified training. return 0 otherwise
@app.route("/person_training/<string:net_id>/<string:training_name>", methods=['GET'])
def get_person_training(net_id, training_name):
    records = csv.reader(open("data/"+records_file, "rt"), delimiter=",")
    for row in records:
        if net_id.upper() in row[0] and training_name in row[1]:
            return '1'
        else:
            return '0'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3003)
