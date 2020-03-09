# NYC Tree Data Fetcher
## General Description
A Flask/ Python based app to fetch, process, and send processed data to whichever client wants/ has access to it. Said data is based off of the [2015 NYC tree census data](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh).

## Requirements
General requirements are:
- the app must use Python
- the app must request open source data
- the app must be able to cache the end result.

## Cloning Instructions
You'll need to have at least Python 3.8.1 installed. PyEnv is also recommended in order to manage Python versions as well as the PyEnv-virtualenv plugin.

Clone the repo with your favorite SCM or manually download it
  ```
    git clone https://github.com/wilsonj806/nyc-tree-data-fetcher.git
  ```

## Local Development
### With Docker
This app will be Dockerized from the start. It includes a `DockerFile` and a `docker-compose.yml` file for convenience and so you don't have to fight Python/ pyenv/ etc when you try to set up your local dev environment.

### Without Docker
