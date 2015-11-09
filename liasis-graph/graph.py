#!/usr/bin/env python
"""
A Graph / Digraph implementation in Python.

Each vertice is implemented as a Python dictionary, a data structure that 
associates a given "key" with a "value". In our case a "key" is a string
representing the label of the vertex and the value is a set of "vertex" 
that is connected to the first one.

For example, if we have a graph with two vertices connected (called "A" and 
"B", respectively), we would represent it in the following way:

    { "A": set(["B"]), "B": set(["A"]) }

=========================================

Basic methods:

    void add(vertex)
    void remove(vertex)
    vertex random(vertex)
    void connect(vertexA, vertexB)
    void disconnect(vertexA, vertexB)
    set(vertex) vertices()
    set(vertex) sucessors(vertex)
    set(vertex) predecessors(vertex)
    set(vertex) ajdacents_to(vertex)
    int order()
    int degree(vertex)
    int in_degree(vertex)
    int out_degree(vertex)
       
Complex methods:      
       
    is_regular()
    is_complete()
    is_tree()*
    is_connected()*
    transitive_closure(vertex)*

* Not working because of a wrong implementation of transitive_closure.

=========================================

@author: Fernando Paladini (fnpaladini@gmail.com).
@license: MIT License
"""

import random
from graph_exceptions import NotDigraphError, DigraphError

class Graph(object):

    def __init__(self, vertices={}, digraph=False):
        """ Creates a new graph.

        :param vertices: A dictionary of vertices to be setted as vertices for the new graph.
        :param digraph: True if the graph is a directed graph. Defaults to false.
        :return None
        """
        self._vertices = vertices
        self._digraph = digraph
    
    ########################
    ##  Basic Operations  ##
    ########################

    def add(self, vertex):
        """ Add a vertice to the graph.

        :param vertex: The vertex (in other words, only a string) to be added to the graph.
        :return None
        """
        if vertex not in self._vertices:
            self._vertices[vertex] = set()

    def remove(self, vertex):
        """ Remove a vertice from the graph. 

        If the graph isn't a directed graph (digraph), remove all connections between 
        *vertex* and other vertices of the graph. Otherwise

        :param vertex: The vertex to be removed.
        :return None
        """
        if vertex in self._vertices:
            for v in self._vertices:
                if vertex in self._vertices[v]:
                    self._vertices[v].remove(vertex)
            del self._vertices[vertex]

    def connect(self, vertexA, vertexB):
        """ Connect vertexA to vertexB.

        If the graph is a digraph, vertexA is the origin vertex and vertexB is the destiny
        vertex (in other words, the edge from A to B will be created). If it isn't a 
        digraph, create an edge from vertexA to vertexB AND from vertexB to vertexA. 

        :param vertexA: The origin vertex.
        :param vertexB: The destiny vertex.
        :return None
        """
        if (vertexA in self._vertices) and (vertexB in self._vertices):
            self._vertices[vertexA].add(vertexB)
            if not self._digraph:
                self._vertices[vertexB].add(vertexA)

    def disconnect(self, vertexA, vertexB):
        """ Disconnect vertexA to vertexB.

        If the graph is a digraph, vertexA is the origin vertex and vertexB is the destiny
        vertex (in other words, the edge from A to B will be removed). If it isn't a 
        digraph, remove the edge from vertexA to vertexB AND from vertexB to vertexA. 

        :param vertexA: The origin vertex.
        :param vertexB: The destiny vertex.
        :return None
        """
        if (vertexA in self._vertices) and (vertexB in self._vertices):
            if vertexB in self._vertices[vertexA]:
                self._vertices[vertexA].remove(vertexB)
                if not self._digraph:
                    self._vertices[vertexB].remove(vertexA)

    def vertices(self):
        """ Returns all vertices of the graph. 

        :return Returns a set of vertex containing all vertices of the graph.
        """
        return set(vertex for vertex in self._vertices) # set or vector?

    def random(self):
        """ Return a single random vertex of the graph.

        :return Return a random vertex of the graph.
        """
        return random.choice(list(self._vertices.keys()))

    def adjacents_to(self, vertex):
        """ Return all vertices adjacent to *vertex*.

        If is a digraph, an exception is raised because this method shouldn't be 
        implemented for a digraph.

        :param vertex: The vertex adjacent to all of the returned values.
        :return A set of vertices
        """
        if not self._digraph:
            if vertex in self._vertices:
                return self._vertices[vertex]
            else:
                return set([])
        else:
            raise DigraphError("Digraph doesn't implement adjacents_to method.")

    def order(self):
        """ Return the order of the graph.

        :return A integer represeting the order of the graph.
        """
        return len(self._vertices)

    def predecessors(self, vertex):
        """ Returns all predecessors from *vertex*. 

        If the graph is a digraph, returns all predecessors for the given vertex.
        If not a digraph, raises an exception because not directed graphs doesn't 
        have such method.

        :param vertex: the vertex that you want to get all predecessors.
        :return A set of vertices.
        """
        if self._digraph:
            if vertex in self._vertices:
                return set(v for v in self._vertices if vertex in self._vertices[v])
            else:
                return set()
        else:
            raise NotDigraphError("Not directed graphs doesn't implement predecessors method.")

    def sucessors(self, vertex):
        """ Returns all sucessors from *vertex*. 

        If the graph is a digraph, returns all sucessors for the given vertex. 
        If not a digraph, raises an exception because not directed graphs doesn't 
        have such method.

        :param vertex: the vertex that you want to get all sucessors.
        :return A set of vertices.
        """
        if self._digraph:
            if vertex in self._vertices:
                return self._vertices[vertex]
            else:
                return set()
        else:
            raise NotDigraphError("Not directed graphs doesn't implement sucessors method.")

    def in_degree(self, vertex):
        """ Return the indegree for the given vertex.

        If it's a not directed graph, raises an exception because you don't have 
        indegree for a not directed graph (take a look at degree).

        :param vertex: the vertex that you want to check the indegree.
        :return A integer representing the indegree.
        """
        try:
            return len(self.predecessors(vertex))
        except NotDigraphError:
            raise NotDigraphError("Not directed graphs doesn't implement in_degree method.")

    def out_degree(self, vertex):
        """ Return the outdegree for the given vertex.

        If it's a not directed graph, raises an exception because you don't have 
        outdegree for a not directed graph (take a look at degree).

        :param vertex: the vertex that you want to check the outdegree.
        :return A integer representing the outdegree.
        """
        try:
            return len(self.sucessors(vertex))
        except NotDigraphError:
            raise NotDigraphError("Not directed graphs doesn't implement out_degree method.")

    def degree(self, vertex):
        """ Return the degree for the given vertex.

        If it's a directed graph, raises an exception because you can't check a
        "general degree" for a digraph (take a look at in_degree and out_degree).

        :param vertex: the vertex that you want to check the degree.
        :return A integer representing the degree.
        """
        if not self._digraph:
            if vertex in self._vertices:
                return len(self.adjacents_to(vertex))
            else:
                return 0
        else:
            raise DigraphError("Digraph doesn't implement Degree method. \
                Take a look at in_degree(vertex) and out_degree(vertex).")

    ##########################
    ##  Derived Operations  ##
    ##########################
    ## Only for not digraph ##
    ##########################

    def is_regular(self):
        if self._digraph:
            raise NotImplementedError

        n = self.degree(self.random())
        for vertex in self._vertices:
            if self.degree(vertex) != n:
                return False
        return True

    def is_complete(self):
        if self._digraph:
            raise NotImplementedError
        max_degree = self.order() - 1
        for vertex in self._vertices:
            if self.degree(vertex) != max_degree:
                return False
        return True

    def is_tree(self):
        if self._digraph:
            raise NotImplementedError
        v = self.random()
        return (self.is_connected()) and (not self.__has_cicle_with(v, v, set()))

    def is_connected(self):
        if self._digraph:
            raise NotImplementedError
        rd = self.random()
        transitive = self.transitive_closure(rd)
        return self._vertices == transitive
    
    def transitive_closure(self, vertex):
        if self._digraph:
            raise NotImplementedError

        done = False
        while not done:
            done = True
            for v0, v1s in self._vertices[vertex]:
                old_len = len(v1s)
                for v2s in [g[v1] for v1 in v1s]:
                    v1s |= v2s
                done = done and len(v1s) == old_len

    def transitive_closure(self, vertex):
      if self._digraph:
          raise NotImplementedError
      return self.__search_transitive_closure(vertex, set())

    def __search_transitive_closure(self, vertex, already_visited):
      if self._digraph:
          raise NotImplementedError

      ft = set()
      already_visited.add(vertex)
      for v in self.adjacents_to(vertex):
          if (v not in already_visited):
              ft = ft.union(self.__search_transitive_closure(v, already_visited))
      return ft

    def __has_cicle_with(self, vertex, current_vertex, previous_vertex, already_visited):
        if self._digraph:
            raise NotImplementedError

        if current_vertex in already_visited:
            return current_vertex == vertex

        already_visited.add(current_vertex)
        for v in self.adjacents_to(vertex):
            if v != previous_vertex:
                if __has_cicle_with(vertex, v, current_vertex, already_visited):
                    return True

        already_visited.remove(current_vertex)
        return False