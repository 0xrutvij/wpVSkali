#!/bin/bash

wget -q https://registry.hub.docker.com/v1/repositories/wordpress/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' | tr '}' '
'  | gawk -F: '{print $3}' | gawk '/^[0-9]\.[0-9]\.[0-9]$/' > resources/text.txt
