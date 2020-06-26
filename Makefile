env:
	# This might be nice?
	python3 -m venv env

init: env
	# Tabs are required in Makefiles
	env/bin/pip install -e .

test:
	env/bin/py.test tests

run-sudoku:
	env/bin/python -m sudoku.sudoku

run-brute-force:
	env/bin/python -m sudoku.recursion_back_tick.bruteForce

.PHONY: init test run-sudoku run-brute-force
