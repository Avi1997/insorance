

from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from save_data import mysql_save_toDb
from service import route_functions
import json

# Opening JSON file
f = open('config.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list


# Closing file
f.close()

app = Flask(__name__)
app.config['MYSQL_HOST'] = data['MYSQL_HOST']
app.config['MYSQL_USER'] = data['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = data['MYSQL_PASSWORD']
app.config['MYSQL_DB'] = data['MYSQL_DB']

mysql = MySQL(app)

load_data_to_db = data["load_data_to_db"]


@app.route('/config', methods=['GET'])
def first_time_config():
    if(request.method == 'GET'):
        if load_data_to_db:
            mysql_save_toDb(mysql)
        data = "hello world"
        return jsonify({'data': data})


@app.route('/get-all/policies', methods=['GET'])
def get_policies():
    return jsonify({'data': route_functions(mysql, 'get-all-policies')})

@app.route('/', methods=['PUT'])
def update_policies():
    return jsonify({'data': route_functions(mysql, 'update-policies',request.body)})
# driver function
if __name__ == '__main__':

    app.run(debug=True)
