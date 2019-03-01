PROJECT_CODEBASE_DIR = "search/"
TESTS_DIR = "tests/"
FILES_TO_CHECK = $(PROJECT_CODEBASE_DIR) $(TESTS_DIR)
DOCKER_COMPOSE = docker-compose -f docker/docker-compose.dev.yml
SERVICE_NAME = "app"

help:
	@echo "start                 - builds and/or starts all services"
	@echo "stop                  - stops all running containers belonging to the project"
	@echo "checks                - runs static checks such as linting without running unit tests"
	@echo "tests                 - runs unit tests in debug mode (able to use pdb breakpoints)"
	@echo "all-tests             - runs static checks and unit tests"
	@echo "fix-imports           - silently modifies imports on all project files that do not"
	@echo "                        adhere to project coding standards regarding imports"
	@echo "run                   - only runs the application service (able to use pdb breakpoints)"
	@echo "shell                 - enter the shell of the application service"
	@echo "build                 - builds the application service"
	@echo "---------------------------------------------------------------"
	@echo "make build should be run after adding and removing dependencies"
	@echo "---------------------------------------------------------------"
	@echo "dependency-tree       - show dependency tree"
	@echo "d-tree                - alias for \"dependency-tree\""
	@echo "add-dependency        - add or update a python dependency by specifying a package"
	@echo "                        e.g. make dependency package=flask"
	@echo "                        e.g. make dependency package=flask==1.0.2"
	@echo "add-dev-dependency    - same as \"dependency\" except the package will be installed"
	@echo "                        during development only"
	@echo "remove-dependency     - remove a python dependency by specifying a package"
	@echo "                        e.g. make remove-dependency package=flask"
	@echo "remove-dev-dependency - same as \"remove-dependency\" regarding development dependencies"

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

add-dependency:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "poetry add $(package)"

add-dev-dependency:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "poetry add $(package) --dev"

remove-dependency:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "poetry remove $(package)"

remove-dev-dependency:
	$(DOCKER_COMPOSE) run --rm $(SERVICE_NAME) /bin/bash -c "poetry remove $(package) --dev"

