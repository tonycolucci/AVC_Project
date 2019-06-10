.PHONY: all venv data model

data/throws_clean.csv:
	copydata_bash

data/analysis_data.csv: data/throws_clean.csv
	python3 src/generate_features.py

data: data/analysis_data.csv

models/trained_model.pkl: data/analysis_data.csv
	python3 src/train_model.py

model: models/trained_model.pkl

# Create a virtual environment named pennylane-env
throwstats/Scripts/activate: requirements.txt
	test -d throwstats || virtualenv throwstats
	. throwstats/bin/activate; pip3 install -r requirements.txt
	touch throwstats/bin/activate

venv: throwstats/Scripts/activate

clean-env:
	rm -r throwstats

clean-model:
	rm models/trained_model.pkl

clean: clean-env 

all: venv data model