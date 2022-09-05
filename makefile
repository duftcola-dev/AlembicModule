install:
#mysql deppendencies (with venv active)
	. venv/bin/activate ; sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
	. venv/bin/activate ; pip install mysqlclient
	. venv/bin/activate ; pip install alembic 
	. venv/bin/activate ; pip install pytest
	. venv/bin/activate ; pip freeze > requirements.txt

init:
	alembic init alembic

list:
	alembic list templates

generic_template:
	alembic init --template generic alembic

async_template:
	alembic init --template async alembic

multi_template:
	alembic init --template multidb alembic