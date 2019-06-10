.PHONY: all venv data model

data/throws_clean.csv:
	copydata_bash

data/analysis_data.csv: data/throws_clean.csv
	python src/generate_features.py

data: data/analysis_data.csv

models/trained_model.pkl: data/analysis_data.csv
	python src/train_model.py

model: models/trained_model.pkl

# Create a virtual environment named pennylane-env
throwstats/Scripts/activate: requirements.txt
	test -d throwstats || virtualenv throwstats
	test -d throwstats/Scripts | . throwstats/Scripts/activate
	test -d throwstats/bin | . throwstats/bin/activate
	pip install -r requirements.txt
	test -d throwstats/Scripts | touch throwstats/Scripts/activate
	test -d throwstats/bin | touch throwstats/bin/activate

venv: throwstats/Scripts/activate

clean-env:
	rm -r throwstats

clean-model:
	rm models/trained_model.pkl

clean: clean-env clean-model

all: venv data model