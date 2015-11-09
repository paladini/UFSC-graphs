#
# Try to run tests with nosetests. 
# If 'nose' isn't installed, run tests from Python (using unittest without verbosity).
# 
all: test

coverage:
	nosetests -v --pdb test_digraph.py test_not_digraph.py --with-coverage --cover-html --cover-html-dir=tests_coverage

test: check
	nosetests -v test_digraph.py test_not_digraph.py

check: 
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_digraph.py
	@type nosetests >/dev/null 2>&1 || /usr/bin/env python test_not_digraph.py

test_python:
	@echo '#####################'
	@echo '#   Test_digraph    #'
	@echo '#####################'
	@echo
	@/usr/bin/env python test_digraph.py
	@echo
	@echo
	@echo
	@echo '######################'
	@echo '#  Test_not_digraph  #'
	@echo '######################'
	@echo
	@/usr/bin/env python test_not_digraph.py

clear:
	rm -f .coverage
	rm -rf tests_coverage/
	rm -f *.pyc
	clear
	clear
	clear