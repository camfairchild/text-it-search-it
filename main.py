#!/usr/bin/env python3.9
from flask import Flask, request
from v0 import v0_blueprint
import os

app = Flask(__name__)

app.register_blueprint(v0_blueprint, url_prefix='/v0')

if __name__ == '__main__':
    print("started :)")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))