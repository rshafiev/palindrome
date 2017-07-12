#!/bin/bash
# get the latest version
git clone https://github.com/rshafiev/palindrome.git
#run detached
nohup ./palindrome/palindrome.py &
