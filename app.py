# Std lib import
import os
from pathlib import Path

# Library Imports
import redis
import requests
from flask import Flask, abort
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.exceptions import NotFound

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
  try:
    json = fetcher.check_cache()
    data = Processor.count_per_boro(data = json)
    return { 'data': data }
  except:
    abort(500,'Something went wrong on our end :(')

@app.route('/data/species')
def count_per_species():
  try:
    json = fetcher.check_cache()
    data = Processor.count_species(data = json)
    return { 'data': data }
  except:
    abort(500,'Something went wrong on our end :(')

@app.route('/data/nta')
def count_per_nta():
  try:
    json = fetcher.check_cache()
    data = Processor.count_per_nta(data = json)
    return { 'data': data }
  except:
    abort(500,'Something went wrong on our end :(')

@app.route('/data/<boro>/species')
def quant_boro_species(boro):
  try:
    json = fetcher.check_cache()
    data = Processor.count_by_boro(data = json, boro = boro)
    return { 'data': data }
  except:
    abort(400, 'Bad request, check your query string parameters')

@app.errorhandler(NotFound)
def handle_not_found(e):
  return 'Resource not found.', 404