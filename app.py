from flask import Flask, request
from v0 import v0_blueprint

app = Flask(__name__)

app.register_blueprint(v0_blueprint, url_prefix='/v0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)