from flask import Flask, jsonify
import requests
import services_config
import config

app = Flask(__name__)
services_config.init_app(app)

# -------------------------
# Auth endpoints
# -------------------------

@app.route("/auth/get_token", methods=['GET'])
def auth_get_token():

    params = {
        "client_id": config.CLIENT_ID,
        "client_secret": config.CLIENT_SECRET,
        "audience": "https://test-vcn-ep.appspot.com/",
        "grant_type": "client_credentials"
        }

    headers = {'content-type': "application/json"}

    result = requests.post("https://vcubells.auth0.com/oauth/token", json=params, headers=headers)
    
    return jsonify(result.json())

@app.route('/main', methods=['GET'])
def home():
    # default service
    return 'Soy el servicio principal'

@app.route('/<service>', methods=['GET'])
def back(service):
    url = app.config['SERVICE_MAP'][service]
    res = requests.get(url + '/')
    return res.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
