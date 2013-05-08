#!/bin/bash

function send {
	lowpriority=$2
	curl --cacert class1_class3.crt -o /dev/null -u APIUSER:APIPASSWORD --data-urlencode "text=$1" --data-urlencode "lowpriority=${lowpriority:=false}" https://hickerspace.org/api/ledticker/
}

# send time with low priority
send "$(date +%H:%M)" true

sleep 10

# send fortune with hight priority (default)
send "$(fortune)"
