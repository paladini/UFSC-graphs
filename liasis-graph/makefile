#
# Try to run tests with nosetests. 
# If 'nose' isn't installed, run tests from Python (using unittest without verbosity).
# 
all: run_tests

run_tests: check
	nosetests -v test_digraph.py 
	nosetests -v test_not_digraph.py

check: 
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_digraph.py
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_not_digraph.py

clear:
	rm *.pyc