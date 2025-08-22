#!/bin/bash

# Set the root directory for the project
PROJECT_ROOT="./"

# Create main directory structure
mkdir -p $PROJECT_ROOT/{app/api,tests,config,scripts,docs}

# Create essential files
touch $PROJECT_ROOT/app/__init__.py
touch $PROJECT_ROOT/app/main.py
touch $PROJECT_ROOT/app/config.py

touch $PROJECT_ROOT/.gitlab-ci.yml
touch $PROJECT_ROOT/docker-compose.yml
touch $PROJECT_ROOT/Dockerfile
touch $PROJECT_ROOT/pyproject.toml
touch $PROJECT_ROOT/Makefile
touch $PROJECT_ROOT/README.md
touch $PROJECT_ROOT/.env

# Confirm creation
echo "Project structure created under '$PROJECT_ROOT'."