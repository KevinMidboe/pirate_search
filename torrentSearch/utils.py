#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Author: KevinMidboe
# @Date:   2017-11-01 15:57:23
# @Last Modified by:   KevinMidboe
# @Last Modified time: 2017-11-02 16:20:29

import re
from datetime import datetime

def sanitize(string, ignore_characters=None, replace_characters=None):
	"""Sanitize a string to strip special characters.

	:param str string: the string to sanitize.
	:param set ignore_characters: characters to ignore.
	:return: the sanitized string.
	:rtype: str

	"""
	# only deal with strings
	if string is None:
		return
	
	replace_characters = replace_characters or ''

	ignore_characters = ignore_characters or set()

	characters = ignore_characters
	if characters:
		string = re.sub(r'[%s]' % re.escape(''.join(characters)), replace_characters, string)

	return string

def return_re_match(string, re_statement):
	if string is None:
		return

	m = re.search(re_statement, string)
	if 'Y-day' in m.group():
		return datetime.now().strftime('%m-%d %Y')
	return sanitize(m.group(), '\xa0', ' ')


# Can maybe be moved away from this class
# returns a number that is either the value of multiple_pages
# or if it exceeds total_pages, return total_pages.
def pagesToCount(multiple, total):
	if (multiple > total):
		return total
	return multiple


def humansize(nbytes):
	suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
	i = 0
	while nbytes >= 1024 and i < len(suffixes)-1:
		nbytes /= 1024.
		i += 1
	f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
	return '{} {}'.format(f, suffixes[i])