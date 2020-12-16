# Flask Deployment

This is the flask deployment version of the Python Scrapper

## Pre-requisites

This Flask Project was deployed on Ubuntu 20, for Windows please alternate your commands accordingly

- Python 3.8.x
- Working Terminal
- [Python Virtual Environment](https://docs.python.org/3/library/venv.html)
- Flask
- SQLite3
- Pandas

## Building the project

Similarly to building the original project, the `requirements.txt` have been adjusted for flask deployment, therefore the instructions are the same. All the requirements will be installed with `python3 -m pip install -r requirements.txt` followed by `python3 setup.py build` and `python3 setup.py install`. This should install all the necessary packages for this application. We also need to ensure we have SQLite3 installed, to do that run `sudo apt install sqlite3` which will install the package.

## Running the project

After installing all the packages, we need to ensure we set the `FLASK_APP` variable to `project` as an environment variable. To do that we simply run `export FLASK_APP=project`. After setting our environment, all we need to do is run `flask run` and open our browser. Once our browser is open navigate to http://127.0.0.1:5000 and that is everything.

## TLDR

- Open terminal
- Install SQLite3
    - `sudo apt install sqlite3`
- Activate a fresh Python virtual environment
    - `python3 -m venv <venv_name>`
    - `source <venv_name>/bin/activate`
- Navigate to the folder where you have cloned this repository
- `cd deploy_code`
- `python3 -m pip install -r requirements.txt`
- `python3 setup.py build`
- `python3 setup.py install`
- `export FLASK_APP=project`
- `flask run`
- Open browser
- Navigate to http://127.0.0.1:5000
