#!/bin/bash
# script that takes in a url and displays all HTTP methods the server will accept
curl -sI $1 | sed -n '/Allow: /s/Allow: //p'
