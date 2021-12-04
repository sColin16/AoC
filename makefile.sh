#! /bin/bash

cp template.py $1/$2.py
vim $1/$2.py -c "/#START" -c "normal c2iw" -c "w" -c "startinsert!"
