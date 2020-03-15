# Std lib import
import os
from pathlib import Path

# Library Imports
import redis
import requests
from flask import Flask
from dotenv import load_dotenv

# App Modules
from Fetch import Fetch
from processor.processor import Processor

## Load ENV
load_dotenv()

app = Flask(__name__)

fetcher = Fetch()

@app.route('/')
def initial_ping():
  return """NYC Tree Data Fetcher, Version: 0.0.0"""

@app.route('/fetch-all')
def fetch_all():
  # Check to make sure we're not in docker compose
  json = fetcher.check_cache()
  print('fetched and returning')
  return {
    '_data_length': len(json),
    'data': json
  }

@app.route('/count-per')
def count_per_boro():
  json = fetcher.check_cache()
  data = Processor.return_per_boro(data = json)
  print('fetched and returning')
  return { 'data': data }
