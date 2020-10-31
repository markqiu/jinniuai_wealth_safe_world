.PHONY: docs
install:
	poetry install
update:
	poetry update

test:
	py.test tests

flake8:
	flake8 --ignore=E501,F401,E128,E402,E731,F821 stralib

isort:
	isort -c

coverage:
	py.test --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=dip tests

package:
	poetry build

publish:
	poetry publish

docs:
	mkdocs serve

build_docs:
	mkdocs build

gh-deploy:
	mkdocs gh-deploy
