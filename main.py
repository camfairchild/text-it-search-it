#!/usr/bin/env python3.9
from flask import Flask, request, g
from v0 import v0_blueprint
import os, psycopg2

app = Flask(__name__)

app.register_blueprint(v0_blueprint, url_prefix='/v0')

@app.before_request
def init_db():
    conn = psycopg2.connect(os.getenv('COCKROACH_CONN'), sslrootcert='/app/root.crt' )
    g.conn = conn

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'conn'):
        g.conn.close()

if __name__ == '__main__':
    print("started :)")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))