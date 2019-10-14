from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Soy el servicio backend"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)