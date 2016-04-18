# -*- coding: utf-8 -*-


def flatten(lst):
    """
    >>> flatten([[[1], 2, [3, 4]], 5, [6], [7, 8, 9]])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    l = []
    for item in lst:
        if isinstance(item, list):
            l.extend(flatten(item))
        else:
            l.append(item)

    return l


def uniq(array):
    """
        >>> uniq([1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7, 7, 8, 9])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> uniq((1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7, 7, 8, 9))
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> uniq(['a', 'z', 'a', 'b', 'a', 'z', 'b'])
        ['a', 'z', 'b']
    """
    return list(set(array))


def same_elements(left, right):
    """
        >>> same_elements([1, 2, 3], [3, 2, 1])
        True
        >>> same_elements([1, 2, 3], [1, 2, 3, 4])
        False
    """
    s1 = set(left)
    s2 = set(right)
    if s1 == s2:
        return True
    return False


def without(container, element):
    """
        Returns a version of the container that does not contain
        the specified element(s)
    """
    pass


def union():
    pass


def intersect():
    pass


def difference():
    pass


def index_of(element, lst):
    pass


def last_index_of(element, lst):
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
