# Std lib import
import os
from pathlib import Path

# Library Imports
import redis
import requests
from flask import Flask
from dotenv import load_dotenv

# App Modules

## Load ENV
load_dotenv()

app = Flask(__name__)
# r = redis.Redis(host = 'app-redis')

@app.route('/')
def initial_ping():
  return """NYC Tree Data Fetcher, Version: 0.0.0"""

@app.route('/fetch-all')
def fetch_all():
  # Check to make sure we're not in docker compose
  envPath = os.getenv('APP_TOKEN')
  token = open(envPath, 'r').read() if Path(envPath).exists() else os.getenv('APP_TOKEN')
  headers = { 'X-App-Token': token }
  req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json", headers = headers)

  json = req.json()
  return {
    '_data_length': len(json),
    'data': json
  }