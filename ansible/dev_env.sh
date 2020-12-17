#!/bin/bash

## Updates Source list and Upgrades any new packages
sudo apt update
sudo apt upgrade

## Installs all dependencies for the app to work
sudo apt install software-properties-common -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt install sqlite3 -y
sudo apt install git -y

## Clones the Repo
git clone https://github.com/deviljin112/Python-Scrapper.git

## Enters the repo folder
cd Python-Scrapper/deploy_code/

## Creates and activates python Venv
python3 -m venv venv
source venv/bin/activate

## Installs all dependencies for Flask and App to run
python3 -m pip install -r requirements.txt
python3 -m pip install pluggy flask flask-login flask-sqlalchemy pandas wheel gunicorn
python3 setup.py bdist_wheel
python3 -m pip install dist/itjobswatch_data-0.1-py3-none-any.whl
python3 setup.py build
python3 setup.py install

# Exports the current path to Python to run tests on
export PYTHONPATH=$PWD/

# Tests that the application works
python3 -m pytest

## Exports the correct Flask Environment
export FLASK_APP=project

## User prompt to run the app
echo "=========================================="
echo "If all tests passed run 'flask run'"
echo "It is recommended to run 'tmux'"
echo "Tmux allows Flask to run in the background"
echo "=========================================="
