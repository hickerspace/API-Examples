#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser, re, random, helper

def replaceAll(text, replaceDict):
	for key in replaceDict:
		text = text.replace(key, replaceDict[key])
	return text

def postillon():
	postillon = []

	feed = feedparser.parse("http://feeds.feedburner.com/blogspot/rkEL")
	for entry in feed["entries"]:
		if entry["title"][:10] == "Newsticker":
			# remove html
			ticker = re.sub('<[^<]+?>', '', entry["description"])
			# get newsticker messages
			ticker = re.findall("\+\+\+\+ (.*?) \+\+\+\+", ticker)
			for t in ticker:
				postillon.append(t)

	postillon = map(lambda tickerMessage: helper.replaceSpChars(tickerMessage.encode("utf-8")),
		postillon)[:15]

	selected = []
	try:
		for i in random.sample(range(len(postillon)), min([5, len(postillon)])):
			selected.append(postillon[i])
	except ValueError:
		selected = postillon

	return "Der Postillon: %s" % " +++ ".join(selected)

