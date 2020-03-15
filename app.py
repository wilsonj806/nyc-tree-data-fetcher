# Std lib import
import os
from pathlib import Path

# Library Imports
import redis
import requests
from flask import Flask
from dotenv import load_dotenv

# App Modules
from Fetch import fetch_data
from processor.processor import Processor

## Load ENV
load_dotenv()

app = Flask(__name__)
red_cache = redis.Redis(host = 'app-redis')

@app.route('/')
def initial_ping():
  return """NYC Tree Data Fetcher, Version: 0.0.0"""

@app.route('/fetch-all')
def fetch_all():
  # Check to make sure we're not in docker compose
  json = fetch_data()

  return {
    '_data_length': len(json),
    'data': json
  }

@app.route('/count-per')
def count_per_boro():
  json = fetch_data()
  data = Processor.return_per_boro(data = json)
  return { 'data': data }
