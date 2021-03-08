TEST_COMPOSE=tests/docker-compose.test.yml
HIDE_DOCKER_CLI_DETAILES=COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1

build:
	$(HIDE_DOCKER_CLI_DETAILES) docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart: down build up

logs:
	docker-compose logs -f

build_test:
	$(HIDE_DOCKER_CLI_DETAILES) docker-compose -f $(TEST_COMPOSE) build

test:
	docker-compose -f $(TEST_COMPOSE) up --abort-on-container-exit && \
	docker-compose -f $(TEST_COMPOSE) down || \
	{ docker-compose -f $(TEST_COMPOSE) down; exit 1; }

all: build up build_test test