# How to run
## Run it by dockercompose
```
docker-compose build
docker-compose up
docker-compose down
```

# Get into running docker
```
docker exec -it ${container_id} /bin/bash
python3 app.py
```

# Note
* flower is a web based tool for monitoring and administrating Celery clusters
* There is no point to run flower withour celery

