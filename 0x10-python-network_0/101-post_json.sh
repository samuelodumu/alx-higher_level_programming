#!/bin/bash
# script that sends a json post request to a url passed as the first argument, and displays only the status code of the response
curl -s -X POST -H "Content-Type: application/json" -d `cat $2` $1
