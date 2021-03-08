TEST_COMPOSE=tests/docker-compose.test.yml

build:
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart: down build up

logs:
	docker-compose logs -f

build_test:
	docker-compose -f $(TEST_COMPOSE) build

test:
	docker-compose -f $(TEST_COMPOSE) up --abort-on-container-exit && \
	docker-compose -f $(TEST_COMPOSE) down || \
	{ docker-compose -f $(TEST_COMPOSE) down; exit 1; }
