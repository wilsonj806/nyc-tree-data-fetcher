# Std lib import
import os
from pathlib import Path

# Library Imports
import redis
import requests
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# App Modules
from fetch import Fetch
from processor import Processor

## Load ENV
load_dotenv()

isDev = os.getenv('FLASK_ENV') == 'development'
accepted = '*' if isDev else 'https://wilsonj806.github.io/*'

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, origins = accepted)

fetcher = Fetch()

@app.route('/')
def initial_ping():
  return """NYC Tree Data Fetcher; Version: 0.0.0"""

@app.route('/data')
def fetch_all():
  json = fetcher.check_cache()
  return {
    '_data_length': len(json),
    'data': json
  }

@app.route('/data/count')
def count_per_boro():
  json = fetcher.check_cache()
  data = Processor.count_per_boro(data = json)
  return { 'data': data }

@app.route('/data/species')
def count_per_species():
  json = fetcher.check_cache()
  data = Processor.count_species(data = json)
  return { 'data': data }

@app.route('/data/nta')
def count_per_nta():
  json = fetcher.check_cache()
  data = Processor.count_per_nta(data = json)
  return { 'data': data }

@app.route('/data/<boro>/species')
def quant_boro_species(boro):
  json = fetcher.check_cache()
  data = Processor.count_by_boro(data = json, boro = boro)
  return { 'data': data }
