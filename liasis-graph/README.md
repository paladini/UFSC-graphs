Liasis-Graph
===========

A Graph / Digraph implementation in Python.

## Testing the implementation
The following commands should be run from "liasis-graph" folder (the same folder of this README).

### Algorithm testing
In order to run a test algorithm for the graph, run `make` from your Terminal.

### Unit Testing
In order to run unit tests for the whole application, run `make test` from your Terminal.

### Testin coverage
To check how many functions of the code was covered by tests just run `make coverage`.

## Prerequisites
We've [nose](https://nose.readthedocs.org/en/latest/) as a prerequisite, that's needed for better unit tests (more verbose at output), however you can execute the tests without it. Our makefile already handles that, so you don't have to worry. If you already have *nose* installed we will use it, otherwise we'll run directly from Python.