#!/bin/bash
# print only the response code
curl -s "$1" -w "%{http_code}"
