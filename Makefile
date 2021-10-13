#
# Module: Host Makefile
#
# Copyright(c) 2014-2015, Cyan, Inc. All rights reserved.
#

#
#
# Variables
#
#
SHELL := /bin/bash
VENV := venv

#
#
# variables
#
#
APP_NAME := the_eye
VERSION ?= latest
VENDOR := dave
DOCKER_IMAGE := $(VENDOR)/$(APP_NAME)

DOCKER_RM := docker rm --force
DOCKER_STOP := docker stop --time 1


help::
	@echo "  Variables:"
	@echo "    APP_NAME            :$(APP_NAME)"
	@echo "    VENDOR              :$(VENDOR)"
	@echo "    DOCKER_IMAGE        :$(DOCKER_IMAGE)"
	@echo ""
	@echo "  Build rules:"
	@echo "    clean               : delete temporary files"
	@echo "    prepare-venv        : create a virtualenv and install packages on dev host"
	@echo "    image         	   : build the docker image"
	@echo ""
	@echo "  Test rules:"
	@echo "    test-flake8         : flake8 tests, also covers python3 sytax compliance"
	@echo "    test-pylint         : pylint tests"
	@echo "    coverage            : measure and report code coverage"
	@echo ""
	@echo "  Cleanup rules:"
	@echo "    rm-all-containers   : docker rm -f --volumes all containers"
	@echo ""
	@echo "  Assorted dev rules:"
	@echo "    enter-docker        : exec a bash shell into existing tron container"
	@echo "    clean-docker        : blow away all docker containers (same as rm-all-containers)"
	@echo ""

all: help

#
#
# Build rules
#
#

# delete temporary files
clean:
	rm -rf $(VENV)/
	find . -name \*.pyc -exec rm --force "{}" \;

# create a virtualenv and install required packages on a developer's host
prepare-venv:
	virtualenv --python /usr/bin/python3 $(VENV)
	$(VENV)/bin/pip install pip wheel setuptools
	$(VENV)/bin/pip install -r requirements.txt

image:
	docker build --tag $(DOCKER_IMAGE) .


# exec a bash shell in the already running tron container
enter-docker:
	docker exec --interactive --tty $(the_eye) bash

#
#
# Cleanup commands
#
#

stop-only:
	-$(DOCKER_STOP) $(APP_NAME)

rm-only:
	-$(DOCKER_RM) -f $(APP_NAME)

.PHONY: run
run: prepare-venv
    #venv/bin/python the_eye.py

.PHONY: run-docker
run: image
	docker run --name $(APP_NAME) $(DOCKER_IMAGE):$(VERSION)

clean-docker rm-all-containers:
	docker ps -aq | xargs --no-run-if-empty docker rm --force --volumes

.PHONY: test-flake8
test-flake8: venv
    # not implemented
	# ./$(VENV)/bin/flake8 --config=./common/testing/config/flake8.cfg $(APP_NAME)

.PHONY: test-unit
test-unit:
    # Not implemented
