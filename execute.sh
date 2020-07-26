#!/bin/bash

ansible-playbook localhost.yml
ansible -m ping all
ansible -m ping all
ansible-playbook nagios_setup.yml
