SHELL := /bin/bash

help: ## This help message
	@echo "usage: make [target]"
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m: \2/')"

.PHONY:clean
clean: ## Clean
	@exec rm -rf ./venv

.PHONY:install
install: ## Install
	@exec virtualenv --no-site-packages venv

.PHONY:test
test: ## Test
	@exec pytest

