#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, urllib2, os

def bitcoin():
	url = 'http://api.bitcoincharts.com/v1/markets.json'
	saveFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bitcoin.json")

	data = json.load(urllib2.urlopen(url))

	with open(saveFile) as file:
		lastAvg = json.load(file)["avg"]

	for entry in data:
		if entry["symbol"] == "mtgoxEUR":
			with open(saveFile, "w") as file:
				json.dump(entry, file)

			percentage = ((entry["avg"] - lastAvg) / ((lastAvg + entry["avg"]) / 2) * 100)
			pre = "+" if percentage >= 0 else ""
			ticker = "Bitcoin | %s EUR (%s%s%%)" % (round(entry["avg"], 3), pre, round(percentage, 3))

			return ticker

