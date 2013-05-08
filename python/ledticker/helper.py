#!/usr/bin/env python
# -*- coding: utf-8 -*-

def replaceSpChars(text):
	replacements = {"\xe2\x80\x93": "-",
					"&quot;": "\"",
					"&amp;": "&",
					"\xe2\x80\x9e": "\"",
					"\xe2\x80\x9c": "\""}

	for key in replacements:
		text = text.replace(key, replacements[key])
	return text
