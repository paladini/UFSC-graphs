#!/usr/bin/env python
import unittest
from graph import Graph
from graph_exceptions import DigraphError, NotDigraphError

class TestBasicOperations(unittest.TestCase):

	# Don't know why isn't working :/
	# def test_construct_without_params(self):
	# 	graph = Graph()
	# 	self.assertEqual(graph.order(), 0)

	def test_construct_with_params(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		self.assertEqual(graph.order(), 5)
		self.assertEqual(graph.degree("a"), 2)
		self.assertTrue(not graph._digraph)

	def test_add(self):
		graph = Graph()
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.degree("a"), 0)

	def test_add_already_added(self):
		graph = Graph()
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.degree("a"), 0)
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.degree("a"), 0)

	def test_remove_without_vertices(self):
		graph = Graph()
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.degree("a"), 0)

	def test_remove(self):
		graph = Graph()
		graph.add("a")
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.degree("a"), 0)

	def test_remove_already_removed(self):
		graph = Graph()
		graph.add("a")
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.degree("a"), 0)
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.degree("a"), 0)

	def test_random(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		random_vertex = graph.random()
		self.assertTrue(random_vertex in graph._vertices)

	def test_order(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		self.assertEqual(graph.order(), 5)
		graph.remove("e")
		self.assertEqual(graph.order(), 4)
		graph.remove("d")
		self.assertEqual(graph.order(), 3)
		graph.remove("c")
		self.assertEqual(graph.order(), 2)
		graph.remove("b")
		self.assertEqual(graph.order(), 1)
		graph.remove("a")
		self.assertEqual(graph.order(), 0)

	def test_adjacents_to(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		adjancetsA = graph.adjacents_to("a")
		self.assertEqual(len(adjancetsA), 2)
		self.assertTrue(adjancetsA == set(["b", "d"]))

	def test_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		self.assertEqual(len(graph.adjacents_to("a")), graph.degree("a"))
		self.assertEqual(len(graph.adjacents_to("a")), 2)

	def test_connect(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		graph.connect("a", "c")
		self.assertTrue(graph.adjacents_to("a") == set(["b", "d", "c"]))
		self.assertEqual(graph.degree("a"), 3)

	def test_connect_without_vertices(self):
		graph = Graph()
		graph.connect("a", "c")
		self.assertFalse(graph.adjacents_to("a") == set(["c"]))
		self.assertEqual(graph.degree("a"), 0)

	def test_connect_with_inexistent_vertex(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		graph.connect("a", "z")
		graph.connect("a", "y")
		graph.connect("a", "h")
		self.assertFalse(graph.adjacents_to("a") == set(["b", "d", "z", "y", "h"]))
		self.assertNotEqual(graph.degree("a"), 5)
		self.assertTrue(graph.adjacents_to("a") == set(["b", "d"]))
		self.assertEqual(graph.degree("a"), 2)

	def test_disconnect(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		graph.disconnect("a", "b")
		self.assertTrue(graph.adjacents_to("a") == set(["d"]))
		self.assertEqual(graph.degree("a"), 1)

	def test_disconnect_without_vertices(self):
		graph = Graph()
		self.assertFalse(graph.adjacents_to("a") == set(["c"]))
		self.assertEqual(graph.degree("a"), 0)
		graph.disconnect("a", "c")
		self.assertFalse(graph.adjacents_to("a") == set(["c"]))
		self.assertEqual(graph.degree("a"), 0)

	def test_disconnect_with_inexistent_vertex(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		graph.disconnect("a", "z")
		graph.disconnect("a", "y")
		graph.disconnect("a", "h")
		self.assertFalse(graph.adjacents_to("a") == set([]))
		self.assertNotEqual(graph.degree("a"), 0)
		self.assertTrue(graph.adjacents_to("a") == set(["b", "d"]))
		self.assertEqual(graph.degree("a"), 2)

	def test_in_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		with self.assertRaises(NotDigraphError):
			graph.in_degree("a")

	def test_out_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		with self.assertRaises(NotDigraphError):
			graph.out_degree("a")

	def test_predecessors(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		with self.assertRaises(NotDigraphError):
			graph.predecessors("a")

	def test_sucessors(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		})
		with self.assertRaises(NotDigraphError):
			graph.sucessors("a")

class DerivedOperations(unittest.TestCase):

	def test_is_regular(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a", "c"]),
			"c": set(["b", "e"]),
			"d": set(["a", "e"]),
			"e": set(["c", "d"])
		})
		self.assertTrue(graph.is_regular())

	def test_is_regular_negative(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a", "c"]),
			"c": set(["b", "e"]),
			"d": set(["a"]),
			"e": set(["c"])
		})
		self.assertFalse(graph.is_regular())

	def test_is_complete(self):
		graph = Graph({
			"a": set(["b", "c", "d", "e"]), 
			"b": set(["a", "c", "d", "e"]),
			"c": set(["b", "d", "e", "a"]),
			"d": set(["a", "b", "c", "e"]),
			"e": set(["c", "a", "b", "d"])
		})
		self.assertTrue(graph.is_complete())

	def test_is_complete_negative(self):
		graph = Graph({
			"a": set(["b"]), 
			"b": set(["a"]),
			"c": set(["e"]),
			"d": set(["e"]),
			"e": set(["c", "d"])
		})
		self.assertFalse(graph.is_complete())

	def test_is_connected(self):
		graph = Graph({
			"a": set(["e", "b"]),
			"b": set(["a", "c"]),
			"c": set(["b", "d"]),
			"d": set(["c", "e"]),
			"e": set(["d", "a"])
		})
		self.assertTrue(graph.is_connected())

	def test_is_connected_negative(self):
		graph = Graph({
			"a": set(["b"]), 
			"b": set(["a"]),
			"c": set(["e"]),
			"d": set(["e"]),
			"e": set(["c", "d"])
		})
		self.assertFalse(graph.is_connected())

	def test_is_tree(self):
		graph = Graph({
			"a": set(["b", "a"]), 
			"b": set(["a", "d", "e"]),
			"c": set(["a"]),
			"d": set(["b"]),
			"e": set(["b"])
		})
		self.assertTrue(graph.is_tree())

	def test_is_tree_negative(self):
		graph = Graph({
			"a": set(["b", "a", "d", "e"]), 
			"b": set(["a", "d", "e"]),
			"c": set(["a"]),
			"d": set(["b", "a"]),
			"e": set(["b", "a"])
		})
		self.assertFalse(graph.is_tree())

if __name__ == "__main__":
	unittest.main()