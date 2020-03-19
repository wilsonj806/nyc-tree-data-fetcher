# NYC Tree Data Fetcher
## General Description
A Flask/ Python based app to fetch, process, and send processed data to whichever client wants/ has access to it. Said data is based off of the [2015 NYC tree census data](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh).

## Additional Docs
- [DevOps](./docs/DevOps.md)

## Requirements
General requirements are:
- the app must use Python
- the app must request open source data
- the app must be able to cache the end result.

## Available Routes
- [Count of trees per borough](https://nyc-tree-data-fetcher.herokuapp.com/data/count)
- [Count of species of trees](https://nyc-tree-data-fetcher.herokuapp.com/data/species)

## Cloning Instructions
You'll need to have at least Python 3.8.1 installed. PyEnv is also recommended in order to manage Python versions as well as the PyEnv-virtualenv plugin.

Clone the repo with your favorite SCM or manually download it
  ```
    git clone https://github.com/wilsonj806/nyc-tree-data-fetcher.git
  ```

## Local Development
### The .env file
A `.env` is required for the project and will require at least two or all three of the below:
```env
  IS_DOCKER=true
  FLASK_ENV=development
  APP_TOKEN=secret
```

The `APP_TOKEN` key isn't added here if you're using Docker Compose. If you are using Docker Compose, follow the [Docker docs instructions](https://docs.docker.com/engine/swarm/secrets/#use-secrets-in-compose) on adding secrets to your `docker-compose.yml` file and add an `app_token.txt` file with the token.

### With Docker
This app will be Dockerized from the start. It includes a `DockerFile` and a `docker-compose.yml` file for convenience and so you don't have to fight Python/ pyenv/ etc when you try to set up your local dev environment.

### Without Docker
Once you clone the repo you'll need to change directory into the project directory and run the below to setup the virtual environment:
```
  python -m venv venv
```

Then activate the virtual envrionment:
```
. venv/bin/activate
```

Then install packages
```
  venv/bin/pip install -r requirements.txt
```

To test it, run flask with the below:
```
  flask run
```