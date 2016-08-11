
.PHONY: dev test clean

dev:
	python3 setup.py develop

test:
	python3 -m py.test --doctest-modules pyATK/ --cov=pyATK/ --cov-report=html

clean:
	rm -rf *.pyc