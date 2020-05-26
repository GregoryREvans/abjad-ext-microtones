.PHONY: docs build help
.DEFAULT_GOAL := help

project = abjadext
errors = E123,E203,E265,E266,E501,W503
origin := $(shell git config --get remote.origin.url)
formatPaths = ${project}/ tests/ *.py
testPaths = ${project}/ tests/

help:  ## Display this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

black-check:
	black --target-version py36 --exclude '.*boilerplate.*' --check --diff ${formatPaths}

black-reformat:
	black --target-version py36 --exclude '.*boilerplate.*' ${formatPaths}

build:  ## Build distribution archive
	python setup.py sdist

clean:  ## Remove transitory files
	find . -name '*.pyc' | xargs rm
	find . -name __pycache__ | xargs rm -Rf
	rm -Rif *.egg-info/
	rm -Rif .cache/
	rm -Rif .tox/
	rm -Rif build/
	rm -Rif dist/
	rm -Rif htmlcov/
	rm -Rif prof/

docs:  ## Build the docs
	make -C docs/ html

flake8:  ## Run flake8
	flake8 --max-line-length=90 --isolated --ignore=${errors} ${formatPaths}

gh-pages:  ## Upload docs to GitHub pages
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

isort:  ## Run isort
	isort \
		--case-sensitive \
		--multi-line 3 \
		--recursive \
		--skip ${project}/__init__.py \
		--skip-glob '*boilerplate*' \
		--thirdparty uqbar \
		--trailing-comma \
		--use-parentheses -y \
		${formatPaths}

mypy:  ## Run mypy
	mypy --ignore-missing-imports ${project}/

pytest:  ## Run pytest
	rm -Rf htmlcov/
	pytest \
		--cov-config=.coveragerc \
		--cov-report=html \
		--cov-report=term \
		--cov=${project}/ \
		--durations=20 \
		${testPaths}

pytest-x:  ## Run pytest and stop on first failure
	rm -Rf htmlcov/
	pytest \
		-x \
		--cov-config=.coveragerc \
		--cov-report=html \
		--cov-report=term \
		--cov=${project}/ \
		--durations=20 \
		${testPaths}

reformat: isort black-reformat ## Reformat codebase via isort and black

release: docs clean build ## Make a new release
	pip install -U twine
	twine upload dist/*.tar.gz
	make gh-pages

test: black-check flake8 mypy pytest ## Run all tests
