# Std lib imports
import os
from pathlib import Path

## Lib Imports
import requests
from dotenv import load_dotenv

def fetch_data():
  # Check to make sure we're not in docker compose
  envPath = os.getenv('APP_TOKEN')
  token = open(envPath, 'r').read() if Path(envPath).exists() else os.getenv('APP_TOKEN')
  headers = { 'X-App-Token': token }
  req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json", headers = headers)

  json = req.json()

  return json

class Fetch:
  def check_cache(self, keyname):
    # if keyname not in cache call fetch_fn, cache it
    # else return cache

  def fetch_all_data(self, keyname):
    # Check to make sure we're not in docker compose
    envPath = os.getenv('APP_TOKEN')
    token = open(envPath, 'r').read() if Path(envPath).exists() else os.getenv('APP_TOKEN')
    headers = { 'X-App-Token': token }
    req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json", headers = headers)

    json = req.json()

    return json