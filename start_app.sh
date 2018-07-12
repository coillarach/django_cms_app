#!/bin/bash
cd ~/django_cms_app
source env/bin/activate
sudo $(which python) manage.py runserver 0.0.0.0:80
