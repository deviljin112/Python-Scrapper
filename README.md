# Python Scrapper

The aim of this project is to create an automated deployment system for the [Python Scrapper](task.md) using AWS with Ansible and Jenkins.

## Pre-requisites

- Python 3.x
- Terminal (Linux preferred although will work on Windows)
- [Python Virtual Environment](https://docs.python.org/3/library/venv.html) (highly recommended)

## Building the project

To test that the app works locally we need to firstly open our terminal (with our virtual environment activated) and navigate to where we have our Python_Scrapper cloned. Next we need to add this folder to PYTHONPATH so that we can run our tests locally without any PATH issues, to do that simply run `export PYTHONPATH="$PWD/"` (Linux only, for Windows see [here](https://www.freecodecamp.org/news/how-to-edit-pythonpath-on-windows-eafd19840d44/)). After we have added our PYTHONPATH, we need to build and install the requirements and dependencies. To do that firstly run `python setup.py build` followed by `python setup.py install`, this will build and install the project and you will notice new folders being created. After we have successfully installed all the dependencies, we can run `python main.py` to use our program, or if we want to test that all the functionality is running correctly we can use `pytest tests/` which will give us the results.

## TLDR

- Open terminal with venv activated
- `cd Python_Scrapper`
- `export PYTHONPATH="$PWD/"`
- `python setup.py build`
- `python setup.py install`

To use:

- `python main.py`

To test:

- `pytest tests/`
