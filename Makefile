PROJECT_CODEBASE_DIR = "search/"
TESTS_DIR = "tests/"
FILES_TO_CHECK = $(PROJECT_CODEBASE_DIR) $(TESTS_DIR)
DOCKER_COMPOSE = docker-compose -f docker/docker-compose.dev.yml
SERVICE_NAME = "app"

help:
	@echo "start                 - builds and/or starts all services"
	@echo "stop                  - stops all running containers belonging to the project"
	@echo "checks                - runs static checks such as linting without running unit tests"
	@echo "tests                 - runs unit tests in debug mode"
	@echo "all-tests             - runs static checks and unit tests"
	@echo "fix-imports           - automatically formats imports in all python files"
	@echo "run                   - only runs the application service (debugging enabled)"
	@echo "shell                 - enter the shell of the application service"
	@echo "build                 - builds the application service"
	@echo "dependency-tree       - show dependency tree"
	@echo "d-tree                - alias for \"dependency-tree\""

start:
	 $(DOCKER_COMPOSE) up

stop:
	$(DOCKER_COMPOSE) down -v

checks:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "\
	echo \"Running checks...\" && \
	echo \"- check for breakpoints\" && \
	source scripts/find-breakpoints.sh && \
	echo \"- mypy\" && \
	mypy $(FILES_TO_CHECK) && \
	echo \"- flake8\" && \
	flake8 $(FILES_TO_CHECK) && \
	echo \"- pylint\" && \
	pylint --rcfile=setup.cfg $(FILES_TO_CHECK) && \
	echo \"All checks completed\" \
	"

.PHONY: tests
tests:
	$(DOCKER_COMPOSE) run --rm --service-ports $(SERVICE_NAME) /bin/bash -c \
	"pytest -s --pdbcls=IPython.terminal.debugger:Pdb -vv"

all-tests: checks tests

fix-imports:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "isort -y"

.PHONY: run
run:
	$(DOCKER_COMPOSE) run --rm --service-ports $(SERVICE_NAME)

shell:
	$(DOCKER_COMPOSE) run --rm --service-ports $(SERVICE_NAME) /bin/bash

build:
	$(DOCKER_COMPOSE) build $(SERVICE_NAME)

dependency-tree:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "poetry show --tree"

d-tree: dependency-tree  # alias for dependency-tree
