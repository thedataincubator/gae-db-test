SHELL=bash
CONDA_ENV=source activate gae-db-test

conda:
	conda env update --name gae-db-test --file environment.yaml

lib:
	$(CONDA_ENV) && pip install -t lib -r requirements.txt

server: lib
	dev_appserver.py app.yaml --admin_port 8001 --port 8081
