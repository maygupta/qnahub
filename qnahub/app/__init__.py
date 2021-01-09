# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

from app import routes