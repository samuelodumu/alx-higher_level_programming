#!/bin/bash
# script that takes in a url and displays the size of the body of the response
curl -s -w "%{http_code}" -o temp_body.txt http://example.com | { read code; if [ "$code" -eq 200 ]; then cat temp_body.txt; fi; rm temp_body.txt; }
