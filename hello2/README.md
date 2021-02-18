# How to run
## Run it locally
```
export FLASK_APP=hello.py && flask run
```

## Run it by docker
```
docker build -t myflask .
docker run -it --rm -p5051:5000 myflask
docker run -d --rm -p5051:5000 myflask
```

## Clean up
```
docker stop ${container_id}
docker rm ${container_id}
```

## Run it by dockercompose
```
docker-compose build
docker-compose up
docker-compose down
```

# Get into running docker
```
docker exec -it ${container_id} /bin/bash
```

