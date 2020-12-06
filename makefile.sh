#! /bin/bash

cp template.py $1/$2.py
vim $1/$2.py -c "%s/xx/$2" -c "normal 7j" -c "startinsert"
