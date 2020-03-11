# Std lib import
import os

# Library Imports
import requests
from flask import Flask
from dotenv import load_dotenv

# App Modules

## Load ENV
load_dotenv()

app = Flask(__name__)

@app.route('/')
def initial_ping():
  return """NYC Tree Data Fetcher, Version: 0.0.0"""

@app.route('/fetch-all')
def fetch_all():
  headers = { 'X-App-Token': os.getenv("TOKEN_SECRET") }
  req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json", headers = headers)

  json = req.json()
  return {
    '_data_length': len(json),
    'data': json
  }