APP_NAME = cars_api
RUN_IN_CONTAINER=docker-compose run --rm -u `id -u`:`id -u` $(APP_NAME)
TEST_COMPOSE=tests/docker-compose.test.yml

build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

build_test:
	docker-compose -f tests/docker-compose.test.yml build

test:
	docker-compose -f $(TEST_COMPOSE) --env-file tests/.env up --abort-on-container-exit && \
	docker-compose -f $(TEST_COMPOSE) down || \
	{ docker-compose -f $(TEST_COMPOSE) down; exit 1; }

clean:
	docker system prune -f

format:
	$(RUN_IN_CONTAINER) black .