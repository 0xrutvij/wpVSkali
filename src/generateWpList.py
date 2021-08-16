#! /bin/python3

import requests
import re

response = requests.get("https://registry.hub.docker.com/v1/repositories/wordpress/tags")
tagDictList = response.json()

with open('resources/text.txt', 'w') as outfile:
    for tag in tagDictList:
        if re.match('[0-9]\.[0-9]\.[0-9]$', tag['name']):
            outfile.write(tag['name']+'\n')
