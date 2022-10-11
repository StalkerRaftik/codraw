# Codraw - anime website
<details>
<summary>Картинки</summary>
  
![image](https://user-images.githubusercontent.com/24423216/159034694-3a12f103-90d8-496c-bcfc-39af1421b11e.png)
![image](https://user-images.githubusercontent.com/24423216/159121701-5f0f6c69-3840-44ac-ad63-db9071a0a8b5.png)
![image](https://user-images.githubusercontent.com/24423216/159035798-6f2e7bf8-48ff-4409-8b87-697058c82358.png)
![image](https://user-images.githubusercontent.com/24423216/159035906-3d8b5796-1b9d-4d67-93a8-5794b51977a9.png)
  
</details>

## Requirements:
1. Docker/docker-compose/buildkit:  [linux](https://docs.docker.com/engine/install/ubuntu/) or [windows](https://www.docker.com/products/docker-desktop/)

## Start dev server: 
1. Go to `codraw/dev` folder;
2. Up containers:
    1. Linux: `COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose up --build`
    2. Windows: `docker-compose up`
3. It's done!


## Celery scheduler:
2. Start redis via `docker-compose up redis`
3. Start beat via `celery -A codraw beat` (only in project container)
4. Create workers via `celery -A codraw worker --loglevel=debug --concurrency=*YOUR WORKERS COUNT*`(only in project container)


## Useful Commands:
- Run tests: `tox`
- Load anime data from csv file: `python manage.py loadcsv path/to/dataset.csv *threads number*` (only in project container)

Supported dataset: [Dataset](https://www.kaggle.com/marlesson/myanimelist-dataset-animes-profiles-reviews/code).

### How to execute commands in project container:
1. Start container
2. Run `docker ps`
3. Run `docker exec -it *CONTAINER NAME* /bin/bash`

### Additional information
* OpenAPI schema: `localhost:8000/api/endpoint`
