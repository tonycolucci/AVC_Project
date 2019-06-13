.PHONY: all venv data model app

data/throws_clean.csv:
	copydata_bash

data/analysis_data.csv: data/throws_clean.csv
	python src/generate_features.py

data: data/analysis_data.csv

models/trained_model.pkl: data/analysis_data.csv
	python src/train_model.py

model: models/trained_model.pkl

# Create a virtual environment named throwstats
throwstats/bin/activate: requirements.txt
	test -d throwstats || virtualenv throwstats
	. throwstats/bin/activate; pip install -r requirements.txt
	touch throwstats/bin/activate

venv: throwstats/bin/activate

clean-env:
	if [ -d throwstats ]; then rm -r throwstats; fi

clean-model:
	if [ -f models/trained_model.pkl ]; then rm models/trained_model.pkl; fi

clean: clean-env clean-model

app:
	python run.py

app_local:
	python run_local.py

prep: venv data model

all: clean prep app