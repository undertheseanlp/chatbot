#!/usr/bin/env bash
git pull origin beta
source activate underthesea.demo.beta
pip uninstall -y underthesea
pip install https://github.com/magizbox/underthesea/archive/beta.zip
underthesea data
python manage.py runserver 0.0.0.0:9001