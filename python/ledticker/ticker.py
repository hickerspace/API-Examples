#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, datetime, json
from indymedia import indymedia
from bitcoin import bitcoin
from postillon import postillon

API_URL = "https://hickerspace.org/api/ledticker/"
API_USER = "APIUSER"
API_PASSWORD = "APIPASSWORD"

def sendToTicker(message, lowPriority=False):
	passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
	passman.add_password(None, API_URL, API_USER, API_PASSWORD)
	urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
	req = urllib2.Request(API_URL)
	resp = json.load(urllib2.urlopen(req, urllib.urlencode({ "text": message, "lowpriority": lowPriority })))

	if not resp["success"]:
		print 'Sending "%s" failed. Response was: "%s"' % (message, resp)

def isRoomOpen():
	url = "https://hickerspace.org/api/room"
	room = json.load(urllib2.urlopen(url))
	return room["roomStatus"] == "open"


now = datetime.datetime.now()

if now.minute == 0:
	if isRoomOpen():
		sendToTicker(postillon())
	else:
		sendToTicker(indymedia())

elif now.minute == 30:
	if isRoomOpen():
		sendToTicker(bitcoin())
	else:
		sendToTicker(indymedia())

elif 31 <= now.minute <= 32:
	pass

else:
	# write time with low priority
	sendToTicker(now.strftime('%H:%M'), True)

