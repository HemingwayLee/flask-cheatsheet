# How to run
## Run it by dockercompose
```
docker-compose build
docker-compose up
docker-compose down
```

# Get into running docker
```
docker exec -it ${container_id} /bin/sh
```

# Redis cli
## Command line usage
```
$ redis-cli -h localhost -p 6379 ping
PONG
```

## Run command with file
```
cd /home/
cat commands.txt | redis-cli 
OK
(integer) 46
```

## Run command remotely
```
$ echo "keys *" | redis-cli -h localhost -p 6379
(empty array)
```

## Interactive mode
```
$ redis-cli
127.0.0.1:6379> keys *
(empty array)
```

# String
```
127.0.0.1:6379> set foo 1
OK
127.0.0.1:6379> get foo
"1"
127.0.0.1:6379> keys * 
1) "foo"
127.0.0.1:6379> set foo 2
OK
127.0.0.1:6379> get foo
"2"
127.0.0.1:6379> keys * 
1) "foo"
127.0.0.1:6379> strlen foo
(integer) 1
```


