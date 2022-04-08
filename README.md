# Codraw - anime website
<details>
<summary>Картинки</summary>
  
![image](https://user-images.githubusercontent.com/24423216/159034694-3a12f103-90d8-496c-bcfc-39af1421b11e.png)
![image](https://user-images.githubusercontent.com/24423216/159121701-5f0f6c69-3840-44ac-ad63-db9071a0a8b5.png)
![image](https://user-images.githubusercontent.com/24423216/159035798-6f2e7bf8-48ff-4409-8b87-697058c82358.png)
![image](https://user-images.githubusercontent.com/24423216/159035906-3d8b5796-1b9d-4d67-93a8-5794b51977a9.png)
  
</details>

Sweety pet project :3
## Installation for dev: 
1. Create virtual environment (`venv`) with Python `3.9.0` or greater;
2. Activate venv using command `source path-to-venv-folder/bin/activate`;
3. Go to root project folder;
4. Run `./setup.sh` command with `sudo` rights;
5. Run `pip install -U -r requirements.txt`
6. Migrate using  `python manage.py migrate`
7. Go to `cofront` folder;
8. Run `yarn` command.
9. Run `sudo yarn global add @vue/cli`
#### It's done!

## Commands:
- Start backend in dev mode: `python manage.py runserver`
- Start frontend in dev mode: `npm run server`
- Run tests: `tox`

- Load anime data from csv file: `python manage.py loadcsv path/to/dataset.csv`

Supported dataset: [Dataset](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews/code).

## Additional information
* OpenAPI schema: `localhost:8010/api/endpoint`
