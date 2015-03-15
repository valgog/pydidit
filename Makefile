.PHONY: clean

clean:
	find . -depth 1 -type d \( -name 'venv*' -or -name dist -or -name '*.egg-info' \) -exec rm -rf '{}' +

venv:
	virtualenv venv
	bash -c ". venv/bin/activate \
	pip install --editable ."

venv3:
	pyvenv venv3
	bash -c ". venv3/bin/activate \
	pip3 install --editable ."

test: venv
	bash -c ". venv/bin/activate \
	pyflakes pydidit && didit \
	deactivate"
