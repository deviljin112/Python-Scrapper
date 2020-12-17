# Web Scrapper

The aim of this project is to create a fully automated deployment system for both the development and production environments.

## Breakdown

The project is a python web scrapper which pulls the top 30 job roles and all the information from ["ITJobsWatch"](https://www.itjobswatch.co.uk) this data is then saved in a csv file.

*Base project's full explanation can be found [here](deploy_code/task.md)*

</br>

The project has two seperate deployments, one for the terminal based version and one which utilises Flask for a web application. Full explanations can be found in their respective files:

- [Terminal](deploy_code/README.md)
- [Flask](deploy_code/FLASK_README.md)

## Development environment

In order to create an ansible ready environment simply run [ansible_controller.sh](ansible/ansible_controller.sh) on your machine to be able to use the ansible platform for deploying the Flask Machine.

</br>

If you would prefer to work on the Flask Machine locally and develop further the application, you can also just run the [dev_env.sh](ansible/dev_env.sh) file on your Linux machine, and this will automate the process of creating all the files installing necessary packages and running the project.

## Ansible

This repo also contains Ansible-Ready files to fully deploy the Flask application. [scrapper_playbook.yaml](ansible/scrapper_playbook.yaml) will deploy the Flask application on the specified machine into production, therefore running `ansible-playbook scrapper_playbook.yaml` will take care of the entire provisioning of your machine. Please ensure that you add `scrapper` group to your hosts file, located in `/etc/ansible/hosts`.

</br>

Example:

```conf
[scrapper]
192.168.0.1 ansible_connection=ssh ansible_ssh_private_key_file=/path/to/file/key.pem
```
