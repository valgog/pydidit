.PHONY: clean

clean:
	if [ -d venv ] ; then rm -rf venv ; fi

venv:
	virtualenv venv
	bash -c ". venv/bin/activate \
	pip install --editable ."

test: venv
	bash -c ". venv/bin/activate \
	pyflakes pydidit && didit \
	deactivate"
