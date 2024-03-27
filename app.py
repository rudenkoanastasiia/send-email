import flask
from flask_cors import CORS, cross_origin
from flask import request
import datetime
import json
import yaml
import subprocess
from cerberus import Validator
from bson.objectid import ObjectId


##############################################################################################
### Read secrets
##############################################################################################

#secrets = subprocess.check_output(['sops', "-i", "-d","secrets.enc.yaml"])
#secrets_dec = yaml.load (secrets, Loader=yaml.SafeLoader)


##############################################################################################
### Error handler
##############################################################################################
    
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

app = flask.Flask(__name__, template_folder='templates')
CORS(app)

##############################################################################################
### Schema of json message
##############################################################################################


schema = {
    'action': {
        'type': 'string',
        'required': True,
        'empty' : False
            },
    'name':{
        'type': 'string',
        'empty' : False
            },
    'groups':{
        'type': 'list'
            }
}

##############################################################################################
### Functions
##############################################################################################

def validate(message):
    valid = Validator()
    valid_message = valid.validate(message, schema)
    if valid_message:
        return valid_message
    else:
        keys = valid.errors.keys()
        raise AuthError({"code": "schema_validation_error",
                    "description": valid.errors
                }, 418)

##############################################################################################
### Routes
##############################################################################################

# test
@app.route('/api/login')
@cross_origin(headers=["Content-Type", "Authorization"])

def login():
    return "I'm so Happy"


@app.route('/api/message', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
def get_message():
    message = request.get_json()
    validate(message)
    return message

##############################################################################################
### Run the app
##############################################################################################

app.run(host='0.0.0.0' , port=5000, debug=True)