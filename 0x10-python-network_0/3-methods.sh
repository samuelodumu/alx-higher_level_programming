#!/bin/bash
# script that takes in a url and displays all HTTP methods the server will accept
curl -s -X OPTIONS $1
