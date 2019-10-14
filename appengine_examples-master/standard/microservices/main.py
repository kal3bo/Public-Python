from flask import Flask
import requests
import services_config

app = Flask(__name__)
services_config.init_app(app)

@app.route('/', methods=['GET'])
def home():
    # default service
    return 'Soy el servicio principal y uso Cloud Build de manera automática'

@app.route('/<service>', methods=['GET'])
def back(service):
    url = app.config['SERVICE_MAP'][service]
    res = requests.get(url + '/')
    return res.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
