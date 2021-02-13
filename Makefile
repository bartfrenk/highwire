.DEFAULT_GOAL := help
.PHONY: build clean docs help publish test report .check-version

NAME := emporium

help: ## Show this help
	@echo "${NAME}"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

##

all: ## Generate all artifacts
all: build docs

init: ## Set up the environment
	@for req in requirements/*.txt; do \
	   pip install -r $$req; \
	done

clean: ## Remove generated artifacts
	@rm -rf build dist *.egg-info docs/build
	@rm -f VERSION

version: ## Generate the VERSION file
	@git describe --tag --always | tee VERSION

build: ## Build the package
build: .check-version
	@python setup.py sdist

test: ## Test the package
	@python setup.py pytest

report: ## Report coverage
	@-pylint src/emporium test/test_emporium
	@coverage run --source src -m pytest
	@coverage report -m

docs: ## Build the documentation
	@make -C docs html

publish: ## Publish the package to PyPI
	@twine upload dist/* --repository-url https://upload.pypi.org/legacy/ \
						 -u ${PYPI_USER} -p ${PYPI_PASSWORD} \
						 --skip-existing

.check-version:
	@if [ ! -f VERSION ]; then \
		echo "Run 'make version' to create a VERSION file"; \
		exit 1; \
	fi;
