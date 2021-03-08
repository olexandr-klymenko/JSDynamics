## Requirements

* docker with docker-compose


## Building the container

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```
To play with API open `http://127.0.0.1:8002/docs` in browser:

## Running the tests
```sh
make build_test
make test
```

## Stop the container
```sh
make down
```