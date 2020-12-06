#! /bin/bash

curl --cookie "session=$AoCsession" https://adventofcode.com/$1/day/$2/input > $1/$2-input.txt
