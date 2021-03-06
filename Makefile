PHONY: format up down logs clean build

APP_NAME = cars_api
RUN_IN_CONTAINER=docker-compose run --rm -u `id -u`:`id -u` $(APP_NAME)

build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

up:
	docker-compose --env-file ./config/.env.app up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	docker-compose down && docker-compose --env-file ./config/.env.test up -d && docker-compose exec tests pytest -p no:cacheprovider -vvv tests

clean:
	docker system prune -f

format:
	$(RUN_IN_CONTAINER) black .