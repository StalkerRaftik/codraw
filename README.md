# Codraw - anime website
Sweety pet project :3
## Installation: 
1. Create virtual environment (`venv`) with Python `3.9.0` or greater;
2. Activate venv using command `source path-to-venv-folder/bin/activate`;
3. Go to root project folder;
4. Run `./setup.sh` command with `sudo` rights;
5. Go to `cofront` folder;
6. Run `yarn` command.
#### It's done!

## Commands:
- Start backend in dev mode: `python manage.py runserver`
- Start frontend in dev mode: `npm run server`
- Run tests: `tox`

- Load anime data from csv file: `python manage.py loadcsv path/to/dataset.csv`

Supported dataset: [Dataset](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews/code).

## Additional information
* OpenAPI schema: `backendIp:backendPort/api/endpoint`