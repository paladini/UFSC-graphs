#!/usr/bin/env python
"""
Implementation of graphs exceptions.

These classes (DigraphError and NotDigraphError) will be useful to raise exceptions when the graph structure don't support a given operation. For example, this can happen when you try to call "degree" method for a non-directed graph. 

Check out the documentation for each method implemented in 'graph.py', it will show you whether an exception is raised or not.
"""
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