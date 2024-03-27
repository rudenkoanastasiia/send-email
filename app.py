import flask
from flask_cors import CORS, cross_origin
import datetime
import json
import yaml
import subprocess

##############################################################################################
### Read secrets
##############################################################################################

#secrets = subprocess.check_output(['sops', "-i", "-d","secrets.enc.yaml"])
#secrets_dec = yaml.load (secrets, Loader=yaml.SafeLoader)

##############################################################################################

app = flask.Flask(__name__, template_folder='templates')
CORS(app)

##############################################################################################
### Routes
##############################################################################################

# test
@app.route('/api/login')
@cross_origin(headers=["Content-Type", "Authorization"])

def login():
    return "I'm so Happy"


##############################################################################################
### Run the app
##############################################################################################

app.run(host='0.0.0.0' , port=5000, debug=True)