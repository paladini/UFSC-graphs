#!/usr/bin/env python
import unittest
from graph import Graph
from graph_exceptions import DigraphError, NotDigraphError

class TestBasicOperations(unittest.TestCase):

	def test_construct_with_params(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		}, digraph=True)
		self.assertEqual(graph.order(), 5)
		self.assertEqual(graph.out_degree("a"), 2)
		self.assertTrue(graph._digraph)

	def test_add(self):
		graph = Graph(digraph=True)
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_add_already_added(self):
		graph = Graph(digraph=True)
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)
		graph.add("a")
		self.assertEqual(graph.order(), 1)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_remove_without_vertices(self):
		graph = Graph(digraph=True)
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_remove(self):
		graph = Graph(digraph=True)
		graph.add("a")
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_remove_already_removed(self):
		graph = Graph(digraph=True)
		graph.add("a")
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)
		graph.remove("a")
		self.assertEqual(graph.order(), 0)
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_random(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		}, digraph=True)
		random_vertex = graph.random()
		self.assertTrue(random_vertex in graph._vertices)

	def test_order(self): #nop
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		}, digraph=True)
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
		}, digraph=True)
		with self.assertRaises(DigraphError):
			adjancetsA = graph.adjacents_to("a")
			self.assertEqual(len(adjancetsA), 2)
			self.assertTrue(adjancetsA == set(["b", "d"]))
			raise Exception("Something went wrong in adjacents_to.")

	def test_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set(["a"]),
			"e": set([])
		}, digraph=True)
		with self.assertRaises(DigraphError):
			graph.degree("a")

	def test_connect(self): 
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		graph.connect("a", "c")
		self.assertTrue(graph.predecessors("a") == set(["b"]))
		self.assertTrue(graph.sucessors("a") == set(["b", "d", "c"]))
		self.assertEqual(graph.in_degree("a"), 1)
		self.assertEqual(graph.out_degree("a"), 3)

	def test_connect_without_vertices(self):
		graph = Graph(digraph=True)
		graph.connect("a", "c")
		self.assertFalse(graph.sucessors("a") == set(["c"]))
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_connect_with_inexistent_vertex(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		graph.connect("a", "z")
		graph.connect("a", "y")
		graph.connect("a", "h")
		graph.connect("h", "a")
		self.assertFalse(graph.sucessors("a") == set(["b", "d", "z", "y", "h"]))
		self.assertNotEqual(graph.out_degree("a"), 5)
		self.assertTrue(graph.predecessors("a") == set(["b"]))
		self.assertEqual(graph.in_degree("a"), 1)

	def test_disconnect(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		graph.disconnect("a", "b")
		self.assertTrue(graph.sucessors("a") == set(["d"]))
		self.assertEqual(graph.in_degree("a"), 1)
		self.assertEqual(graph.out_degree("a"), 1)

	def test_disconnect_without_vertices(self):
		graph = Graph(digraph=True)
		self.assertFalse(graph.sucessors("a") == set(["c"]))
		self.assertFalse(graph.predecessors("a") == set(["c"]))
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)
		graph.disconnect("a", "c")
		self.assertFalse(graph.sucessors("a") == set(["c"]))
		self.assertFalse(graph.predecessors("a") == set(["c"]))
		self.assertEqual(graph.in_degree("a"), 0)
		self.assertEqual(graph.out_degree("a"), 0)

	def test_disconnect_with_inexistent_vertex(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		graph.disconnect("a", "z")
		graph.disconnect("a", "y")
		graph.disconnect("a", "h")
		self.assertFalse(graph.sucessors("a") == set([]))
		self.assertFalse(graph.predecessors("a") == set([]))
		self.assertNotEqual(graph.in_degree("a"), 0)
		self.assertNotEqual(graph.out_degree("a"), 0)
		self.assertTrue(graph.sucessors("a") == set(["b", "d"]))
		self.assertTrue(graph.predecessors("a") == set(["b"]))
		self.assertEqual(graph.in_degree("a"), 1)
		self.assertEqual(graph.out_degree("a"), 2)

	def test_in_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		self.assertEqual(graph.in_degree("a"), 1)

	def test_out_degree(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		self.assertEqual(graph.out_degree("a"), 2)

	def test_predecessors(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		self.assertTrue(graph.predecessors("a") == set(["b"]))
		self.assertEqual(len(graph.predecessors("a")), 1)

	def test_sucessors(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a"]),
			"c": set([]),
			"d": set([]),
			"e": set([])
		}, digraph=True)
		self.assertTrue(graph.sucessors("a") == set(["b", "d"]))
		self.assertEqual(len(graph.sucessors("a")), 2)

class DerivedOperations(unittest.TestCase):

	def test_is_regular(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a", "c"]),
			"c": set(["b", "e"]),
			"d": set(["a", "e"]),
			"e": set(["c", "d"])
		}, digraph=True)
		self.assertTrue(graph.is_regular())

	def test_is_regular_negative(self):
		graph = Graph({
			"a": set(["b", "d"]), 
			"b": set(["a", "c"]),
			"c": set(["b", "e"]),
			"d": set(["a"]),
			"e": set(["c"])
		}, digraph=True)
		self.assertFalse(graph.is_regular())

	def test_is_complete(self):
		graph = Graph({
			"a": set(["b", "c", "d", "e"]), 
			"b": set(["a", "c", "d", "e"]),
			"c": set(["b", "d", "e", "a"]),
			"d": set(["a", "b", "c", "e"]),
			"e": set(["c", "a", "b", "d"])
		}, digraph=True)
		self.assertTrue(graph.is_complete())

	def test_is_complete_negative(self):
		graph = Graph({
			"a": set(["b"]), 
			"b": set(["a"]),
			"c": set(["e"]),
			"d": set(["e"]),
			"e": set(["c", "d"])
		}, digraph=True)
		self.assertFalse(graph.is_complete())

	def test_is_connected(self):
		graph = Graph({
			"a": set(["b"]),
			"b": set(["c"]),
			"c": set(["d"]),
			"d": set(["e"]),
			"e": set(["a"])
		}, digraph=True)
		self.assertTrue(graph.is_connected())

	def test_is_connected_negative(self):
		graph = Graph({
			"a": set(["b"]), 
			"b": set(["a"]),
			"c": set(["e"]),
			"d": set(["e"]),
			"e": set(["c", "d"])
		}, digraph=True)
		self.assertFalse(graph.is_connected())

	def test_is_tree(self):
		graph = Graph({
			"a": set(["b", "a"]), 
			"b": set(["a", "d", "e"]),
			"c": set(["a"]),
			"d": set(["b"]),
			"e": set(["b"])
		}, digraph=True)
		self.assertTrue(graph.is_tree())

	def test_is_tree_negative(self):
		graph = Graph({
			"a": set(["b", "a", "d", "e"]), 
			"b": set(["a", "d", "e"]),
			"c": set(["a"]),
			"d": set(["b", "a"]),
			"e": set(["b", "a"])
		}, digraph=True)
		self.assertFalse(graph.is_tree())

if __name__ == "__main__":
	unittest.main()