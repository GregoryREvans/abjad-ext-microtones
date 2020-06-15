.PHONY: docs build

black-check:
	black --check --diff --target-version=py38 .

black-reformat:
	black --target-version=py38 .

build:
	python setup.py sdist

clean:
	find . -name '*.pyc' | xargs rm
	rm -Rif *.egg-info/
	rm -Rif .cache/
	rm -Rif .tox/
	rm -Rif __pycache__
	rm -Rif build/
	rm -Rif dist/
	rm -Rif htmlcov/
	rm -Rif prof/

docs:
	make -C docs/ html

flake_exclude = --exclude=__metadata__.py
flake_ignore = --ignore=E203,E266,E501,W503
flake_options = --isolated --max-line-length=88

flake8:
	flake8 ${flake_exclude} ${flake_ignore} ${flake_options}

origin := $(shell git config --get remote.origin.url)

gh-pages:
	rm -Rf gh-pages/
	git clone $(origin) gh-pages/
	cd gh-pages/ && \
		git checkout gh-pages || git checkout --orphan gh-pages
	rsync -rtv --del --exclude=.git docs/build/html/ gh-pages/
	cd gh-pages && \
		touch .nojekyll && \
		git add --all . && \
		git commit --allow-empty -m "Update docs" && \
		git push -u origin gh-pages
	rm -Rf gh-pages/

isort-check:
	isort \
	--case-sensitive \
	--check-only \
	--diff \
	--force-grid-wrap=0 \
	--line-width=88 \
	--multi-line=3 \
	--project=abjad \
	--recursive \
	--thirdparty=uqbar \
	--trailing-comma \
	--use-parentheses \
	.

isort-reformat:
	isort \
	--apply \
	--case-sensitive \
	--force-grid-wrap=0 \
	--line-width=88 \
	--multi-line=3 \
	--project=abjad \
	--recursive \
	--thirdparty=uqbar \
	--trailing-comma \
	--use-parentheses \
	.

mypy:
	mypy .

project = abjadext

pytest:
	rm -Rf htmlcov/
	pytest \
	--cov-config=.coveragerc \
	--cov-report=html \
	--cov-report=term \
	--cov=${project}/ \
	--durations=20 \
	.

pytest-x:
	rm -Rf htmlcov/
	pytest \
	-x \
	--cov-config=.coveragerc \
	--cov-report=html \
	--cov-report=term \
	--cov=${project}/ \
	--durations=20 \
	.

reformat:
	make black-reformat
	make isort-reformat

release:
	make clean
	make build
	twine upload dist/*.tar.gz

check:
	make black-check
	make flake8
	make isort-check
	make mypy

test:
	make black-check
	make flake8
	make isort-check
	make mypy
	make pytest
