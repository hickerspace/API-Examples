#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
import random, helper

def replaceSpChars(text):
	replacements = {"\xe2\x80\x93": "-",
					"&quot;": "\"",
					"&amp;": "&",
					"\xe2\x80\x9e": "\"",
					"\xe2\x80\x9c": "\""}

	for key in replacements:
		text = text.replace(key, replacements[key])
	return text

# some conspiracies to mix in
def indymedia():

	conspiracies = ["Mondlandung doch nur vorgetäuscht",
					"Erde vielleicht doch nicht hohl?",
					"Mittelalter doch nur erfunden?",
					"CIA gibt JFK-Attentat zu",
					"Bielefeld nun doch in Google Maps",
					"Endlich: Bibelcode gelöst!",
					"Liest das überhaupt irgendwer?",
					"Bilderberger handeln doch im Sinne der NWO",
					"Aufgedeckt: Macht Lichtnahrung dick?",
					"Sonne doch kalt?",
					"Werwolf auf Marienfriedhof gesichtet",
					"Kornkreis vor Sarstedt gesichtet",
					"Esst mehr Reis!",
					"Flugscheibe über Hildesheimer Innenstadt gesichtet",
					"Erdbebenmaschine erfolgreich getestet"]

	replacements = {"\xe2\x80\x93": "-",
					"&quot;": "\"",
					"&amp;": "&",
					"\xe2\x80\x9e": "\"",
					"\xe2\x80\x9c": "\""}

	parser = etree.XMLParser(ns_clean=True)
	tree = etree.parse("http://de.indymedia.org/RSS/newswire.xml", parser)
	indyEntries = tree.xpath("//ns:item/ns:title", namespaces = { "ns" : "http://purl.org/rss/1.0/" })

	indyEntries = map(lambda indyEntry: helper.replaceSpChars(indyEntry.text.encode("utf-8")),
		indyEntries)[:5]

	rand = random.randint(0, len(conspiracies)-1)
	indyEntries.insert(random.randint(0, len(indyEntries)-1), conspiracies[rand])
	news = " +++ ".join(indyEntries)

	return "Indymedia: %s" % news

