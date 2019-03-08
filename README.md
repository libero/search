# Libero Search
This project is an implementation of Libero search API

## Dependencies

* [Docker](https://www.docker.com/)

## Getting started
This project provides a `Makefile` with short commands to run common tasks.
Typically, MacOS and most Linux distributions come with [gnu make](https://www.gnu.org/software/make/)
installed. If are unable to run the commands below because your system doesn't 
have `gnu make` installed, you can try to install it or copy and paste commands
found in the `Makefile` into your command line interface.

* `make help` for a full list of commands.
* `make start` builds and/or runs the site locally configured for development purposes.
* `make stop` stops containers and cleans up any anonymous volumes.

## Running the tests

* `make tests` runs unit tests.
* `make checks` runs static checks such as: mypy, flake8, pylint.
* `make all-tests` combines the two commands above by running all checks followed
 by unit tests

## Adding and removing dependencies
This project uses [Poetry](https://poetry.eustace.io/) for dependency management.

To [add](https://poetry.eustace.io/docs/cli/#add) and [remove](https://poetry.eustace.io/docs/cli/#remove)
a project dependency, run `make shell` to enter the bash shell of the app container
and make changes as necessary. Any changes made will only update `pyproject.toml`
and `poetry.lock` files. If you would like to apply the changes to the app container
then rebuild the container by running `make build`.

Example:
```bash
$ make shell
bash 4.4# poetry add pytest --dev
(ctrl + d to exit the container shell)
$ make build
```

For a full list of Poetry cli options visit the official documentation [here](https://poetry.eustace.io/docs/cli/)

## Other useful commands

- `make run` Only runs the python service. Useful for debugging with pdb.
- `make shell` Enters the container and presents a bash shell.
- `make dependency-tree` or `make d-tree` Displays a dependency tree.
- `make fix-imports` Automatically format imports for all project python files.

## Getting help

- Report a bug or request a feature on [GitHub](https://github.com/libero/libero/issues/new/choose).
- Ask a question on the [Libero Community Slack](https://libero.pub/join-slack).
- Read the [code of conduct](https://libero.pub/code-of-conduct).
