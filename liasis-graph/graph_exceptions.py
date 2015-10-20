#!/usr/bin/env python

class DigraphError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class NotDigraphError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)