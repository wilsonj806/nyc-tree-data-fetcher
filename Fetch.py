# Std lib imports
import os
import json
from pathlib import Path

## Lib Imports
import redis
import requests
from dotenv import load_dotenv

# Global Module Var
isDocker = os.getenv('IS_DOCKER')

cacheHost = 'app-redis' if isDocker else 'localhost'
red_cache = redis.Redis(host = cacheHost, port = 6379)

class Fetch:
  base_key = 'base'

  def check_cache(self):
    # if keyname not in cache call fetch_fn, cache it
    cachedData = red_cache.get(self.base_key)
    if not cachedData:
      res = self.fetch_all_data()
      strRes = json.dumps(res)
      red_cache.set(self.base_key, strRes)
      return res
    # else return cache
    else:
      return json.loads(cachedData)

  def fetch_all_data(self):
    # Check to make sure we're not in docker compose
    appToken = os.getenv('APP_TOKEN')
    token = open(envPath, 'r').read() if isDocker else appToken

    headers = {
      'X-App-Token': token,
    }
    req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json?$limit=3000", headers = headers)

    res = req.json()

    return res

