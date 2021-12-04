#! /bin/bash

# To execute this script, run `source ./startup.sh year day` (or '.' instead of 'source')

# Get the input
curl --cookie "session=$AoCsession" https://adventofcode.com/$1/day/$2/input > $1/$2-input.txt

# Get the example for the problem
# TODO: consider an automated process to pull the example
# Would need an easy way to enter manually if this fails
echo "Enter the example input:"
cat > $1/$2-example.txt

# Enter the directory for the year
cd $1

# Execute the full solution
python3 $2.py

