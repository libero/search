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

The following commands update files that keep track of project dependencies.

```bash
make add-dependency package=<package name>
make add-dev-dependency package=<package name>

# examples:
make add-dependency package=flask
make add-dependency package=flask==1.0.2
make add-dev-dependency package=pytest
```
These commands add a python package as a project dependency or 
development dependency alike. You can specify just the package name to get the 
latest version or specify a specific version number.

```bash
make remove-dependency package=<package name>
make remove-dev-dependency package=<package name>
```
These commands remove dependencies accordingly.

```bash
make build
```
Will rebuild the python container and persist changes made to dependency files.

## Other useful commands
```bash
make run
```
Use this command to only run the python service.
It is possible to use pdb breakpoints with this configuration.

```bash
make shell
```
Use this to run the python container that would run the application and enter a
bash prompt.

```bash
make dependency-tree
# or
make d-tree
```
Use this to display a dependency tree

```bash
make fix-imports
```
When checks are run warnings are displayed because imports do not follow the
project conventions as specified in `setup.cfg` under `[isort]`.
Use this command to automatically fix imports for all project python files.

## Getting help

- Report a bug or request a feature on [GitHub](https://github.com/libero/libero/issues/new/choose).
- Ask a question on the [Libero Community Slack](https://libero.pub/join-slack).
- Read the [code of conduct](https://libero.pub/code-of-conduct).
