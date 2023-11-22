.PHONY: Usefull commands

SHELL=/bin/bash
BIN := ./.venv/bin
PIP := $(BIN)/pip
PYTHON := $(BIN)/python
PYTEST:=$(BIN)/pytest

.venv:
	python3 -m venv .venv

.PHONY: pip-install
pip-install: requirements.txt .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r $<


.PHONY: build
build:
	$(PYTHON) -m build --sdist

.PHONY: tests
tests: tests
	$(PYTEST) .