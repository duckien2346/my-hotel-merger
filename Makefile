
venv:
	python3 -m venv venv ;\
	. ./venv/bin/activate ;\
	pip install --upgrade pip setuptools wheel;\
	pip install -e .

pylint:
	. ./venv/bin/activate ;\
	pylint --rcfile .pylintrc tap_postgres/
