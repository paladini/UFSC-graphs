#
# Try to run tests with nosetests. 
# If 'nose' isn't installed, run tests from Python (using unittest without verbosity).
# 
all: run

run:


test: check
	nosetests -v test_digraph.py test_not_digraph.py --with-coverage --cover-html --cover-html-dir=tests_coverage

check: 
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_digraph.py
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_not_digraph.py

clear:
	rm *.pyc