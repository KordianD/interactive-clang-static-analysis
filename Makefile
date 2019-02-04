all: clean test

fix:
	autopep8 src --recursive --in-place
	autopep8 test --recursive --in-place

test:
	python -m pytest -vv
	py.test --cov  src test --cov-report term-missing
	flake8 src test --max-line-length 120
	pylint --rcfile=standard.rc --disable=missing-docstring src test
	pyflakes .

clean:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm --force  {} +

.PHONY: clean test