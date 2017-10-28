test:
	python3 -m unittest
	coverage run test_rpn.py
	coverage report -m
	coverage-badge > README.md
.PHONY: test
