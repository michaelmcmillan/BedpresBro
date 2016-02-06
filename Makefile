PYTHON=$(shell which python3)
PYLINT=$(shell which pylint)
PIP=$(shell which pip3)
COVERAGE=$(shell which coverage)
TEST_DIR=./test
SRC_DIR=./src
TEST_FILES=*_test.py
REQUIREMENTS=./.requirements.txt
LINT_CONFIG=./.pylint.rc
MODULES=$(shell pwd)/$(SRC_DIR)
TEST_COMMAND=unittest discover -s $(TEST_DIR) -p $(TEST_FILES)

install:
	@$(PIP) install -r $(REQUIREMENTS) 

run: export PYTHONPATH=$(MODULES)
run: export PYTHONDONTWRITEBYTECODE="false"
run:
	@$(PYTHON) $(SRC_DIR)/runner.py

test: export PYTHONPATH=$(MODULES)
test: export PYTHONDONTWRITEBYTECODE="false"
test: export TEST="true"
test: unit-test clean

ci-test: export PYTHONPATH=$(MODULES)
ci-test: export PYTHONDONTWRITEBYTECODE="false"
ci-test: export TEST="true"
ci-test: coverage lint clean

unit-test:
	@$(PYTHON) -m $(TEST_COMMAND) 

coverage:
	@$(COVERAGE) run --branch --source=$(SRC_DIR) -m $(TEST_COMMAND)
	@$(COVERAGE) report --skip-covered -m

lint:
	@$(PYLINT) --rcfile $(LINT_CONFIG) $(SRC_DIR)/*

clean:
	-@find . -name '.DS_Store'   -delete
	-@find . -name '*.pyc' 		 -delete
	-@find . -name '__pycache__' -delete

.PHONY: test install clean run
