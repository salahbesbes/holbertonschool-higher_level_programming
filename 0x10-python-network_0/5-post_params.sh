#!/bin/bash
# sent data to server
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
