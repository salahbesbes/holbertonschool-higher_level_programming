#!/bin/bash
# print only the response code
curl -s -o /dev/null "$1" -w "%{http_code}"
