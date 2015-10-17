from abc import ABCMeta, abstractmethod, abstractproperty

class Graph(object):
	__metaclass__ = ABCMeta

	@abstractproperty
	def nodes(self):
		return

	@abstractproperty
	def edges(self):
		return

	@abstractmethod
	def containsEdge(self):
		return

	@abstractmethod
	def addEdge(self):
		return

	@abstractmethod
	def removeEdge(self):
		return

	@abstractmethod
	def removeAllEdges(self):
		return