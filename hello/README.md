# How to run
## Run it locally
```
export FLASK_APP=hello.py && flask run
```

## Run it by docker
```
docker build -t myflask .
docker run -it --rm -p5051:5000 myflask
```

## Run it by dockercompose
```
docker-compose build
docker-compose up
docker-compose down
```

# Get into running docker
```
docker exec -it {container id} /bin/bash
```

