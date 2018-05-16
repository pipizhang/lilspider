SHELL := /bin/bash

help: ## This help message
	@echo "Usage: make [target]"
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY:clean
clean: ## Clean
	@exec rm -rf ./venv

.PHONY:install
install: ## Setup Virtualenv
	@exec virtualenv --no-site-packages venv

.PHONY:test
test: ## Run test suites
	@exec pytest

