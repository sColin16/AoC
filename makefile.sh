#! /bin/bash

cp template.py $1/$2.py
vim $1/$2.py -c "%s/xx/$2/g" -c "/#START" -c "normal cc" -c "w" -c "startinsert"
