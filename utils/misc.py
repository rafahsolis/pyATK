# -*- coding: utf-8 -*-


def if_else(condition, valueForTrue, valueForFalse):
	if (condition) is True:
		return valueForTrue
	return valueForFalse




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)