.PHONY: sphinx-doc initial-setup venv smoke-test clean-sphinx-doc data clean

sphinx-doc: clean-sphinx-doc
	. ./venv/bin/activate \
	    && cd doc && sphinx-apidoc -f -o ./source ../apsrm --separate \
	    && rm -f ./source/modules.rst
	sed -i 's/undoc-members/no-undoc-members/g' doc/source/apsrm.rst
	echo "   :imported-members:" >> doc/source/apsrm.rst
	echo "   :imported-members:" >> doc/source/apsrm.ext.rst
	echo "   :imported-members:" >> doc/source/apsrm.ventilation.rst
	. ./venv/bin/activate \
	    && cd doc/source \
	    && PYTHONPATH=$(CURDIR) sphinx-build -b html . ../build

initial-setup: clean venv sphinx-doc

venv: clean
	rm -rf venv
	virtualenv -p python3 venv
	. ./venv/bin/activate && pip install -e .[dev,notebooks]

smoke-test:
	. venv/bin/activate \
		&& pytest ./tests/test_smoke.py

clean-sphinx-doc:
	rm -rf doc/build doc/source/apsrm*

data:
	. venv/bin/activate \
		&& cd data \
		&& python load-emissions.py \
		&& Rscript pcr-beta-bernoulli.R \
		&& Rscript vaccine-efficacy.R

clean: clean-sphinx-doc
	rm -rf build/ dist/ *.egg-info
	find . -name '__pycache__' -type d -exec rm -rf {} +
	find . -type f \( -iname '*.pyc' -o -iname '*.pyo' -o -iname '*~' \) -exec rm -f {} +
