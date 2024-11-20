
venv:
	python3 -m venv venv ;\
	. ./venv/bin/activate ;\
	pip install --upgrade pip setuptools wheel;\
	pip install .

pylint:
	. ./venv/bin/activate ;\
	pylint --rcfile .pylintrc my_hotel_merger/

