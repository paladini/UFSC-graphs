Liasis-Graph
===========

A Graph / Digraph implementation in Python.

## Testing the implementation
P.S: the following commands should be run from "liasis-graph" folder (the same folder of this README).

### Algorithm testing
In order to run a test algorithm for the graph, run `make` from your Terminal.

### Testing coverage
To check how many functions of the code was covered by unit tests just run `make coverage`. This will not work without `nose` and `coverage` (described on the Prerequisites section).

After run `make coverage`, open the file located at `tests_coverage/index.html` to check the results of code coverage.

## Prerequisites
We've [nose](https://nose.readthedocs.org/en/latest/) as a prerequisite, that's needed for better unit tests (more verbose at output), however you can execute the tests without it. Our makefile already handles that, so you don't have to worry. If you already have *nose* installed we will use it, otherwise we'll run directly from Python.

To create the testing coverage you'll need the [coverage](http://nose.readthedocs.org/en/latest/plugins/cover.html) Python module alongside with the `nose` module. Without these two modules, isn't possible to show the percentage of code covered by the unit tests. 