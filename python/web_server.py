"""
$ env FLASK_APP=web_server.py flask run
 * Serving Flask app "web_server"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
"""
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def web_server():
    name = request.args.get("name", "world")
    return f'Hello {escape(name)}!'
