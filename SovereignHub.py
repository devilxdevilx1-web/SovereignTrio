import os
import time
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)
CORE_PATH = "/Users/kanchetidevieswar/hybrid/sovereign_engine_full/SovereignEngine.cpp"
VAL_PATH = "/Users/kanchetidevieswar/hybrid/sovereign_validator"

@app.route('/')
def home():
    return "<h1>SOVEREIGN OPERATIONAL HUB</h1><p>Status: ACTIVE</p>"

@app.route('/audit')
def audit():
    source = "/Users/kanchetidevieswar/linux_source.tar"
    output = subprocess.check_output([VAL_PATH, source]).decode()
    return jsonify({"output": output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
