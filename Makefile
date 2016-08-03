
.PHONY: dev test clean

dev3:
	python3 setup.py develop

dev2:
	python setup.py develop

test3:
	python3 -m py.test --doctest-modules pyATK/ --cov=pyATK/ --cov-report=html

test2:
	python -m py.test --doctest-modules pyATK/ --cov=pyATK/ --cov-report=html

clean:
	rm -rf *.pyc