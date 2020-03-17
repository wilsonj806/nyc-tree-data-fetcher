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

cacheHost = 'redis://app-redis:6379' if isDocker else 'redis://localhost:6379'
isProd = os.getenv('FLASK_ENV') == 'production'

host = os.getenv('REDIS_URL') if isProd else cacheHost
red_cache = redis.from_url(host)

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
    token = open(appToken, 'r').read() if isDocker else appToken

    headers = {
      'X-App-Token': token,
    }
    req = requests.get("https://data.cityofnewyork.us/resource/uvpi-gqnh.json?$limit=3000", headers = headers)

    res = req.json()

    return res

