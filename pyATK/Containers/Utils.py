# -*- coding: utf-8 -*-


class ListsHelper:
    @staticmethod
    def each(cls, collection, callback):
        pass

    @classmethod
    def flatten(cls, collection):
        """
        >>> ListsHelper.flatten([[[1], 2, [3, 4]], 5, [6], [7, 8, 9]])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        """
        l = []
        for item in collection:
            if isinstance(item, list):
                l.extend(cls.flatten(item))
            else:
                l.append(item)
        return l

    @classmethod
    def unique(cls, collection):
        """
            >>> ListsHelper.unique([1, 2, 1, 2, 5, 3, 3, 4, 4, 1, 1, 1, 4, 5, 6, 7, 7, 6, 8, 7, 8, 9])
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
            >>> ListsHelper.unique((1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 7, 7, 7, 7, 8, 9))
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
            >>> ListsHelper.unique(['a', 'z', 'a', 'b', 'a', 'z', 'b'])
            ['a', 'b', 'z']
        """
        return sorted(list(set(collection)))

    @classmethod
    def sameElements(cls, left, right):
        """
            >>> ListsHelper.sameElements([1, 2, 3], [3, 2, 1])
            True
            >>> ListsHelper.sameElements([1, 2, 3], [1, 2, 3, 4])
            False
        """
        s1 = set(left)
        s2 = set(right)
        if s1 == s2:
            return True
        return False

    @classmethod
    def keep(cls, collection, element):
        return list(filter(lambda x: x == element, collection))

    @classmethod
    def without(cls, collection, element):
        """
        >>> ListsHelper.without([1, 2, 3, 4, 5], 5)
        [1, 2, 3, 4]
        >>> ListsHelper.without([1, 2, 3], 2)
        [1, 3]
        """
        return list(filter(lambda x: x != element, collection))

    @classmethod
    def indexOf(cls, collection, element):
        """
        >>> ListsHelper.indexOf("Hello There", 'e')
        1
        >>> ListsHelper.indexOf([0, 2, 3], 1)
        -1
        """
        index = -1
        for item in collection:
            index += 1
            if item == element:
                return index
        return -1

    @classmethod
    def lastIndexOf(cls, collection, element):
        """
        >>> ListsHelper.lastIndexOf([1, 2, 3, 1, 5, 6, 1], 1)
        6
        >>> ListsHelper.lastIndexOf([1, 2, 3, 1, 5, 6, 1], 10)
        -1
        """
        index = -1
        while index < len(collection):
            index += 1
            if element == collection[len(collection) - index - 1]:
                return len(collection) - index - 1
        return -1

    @classmethod
    def reverse(cls, collection):
        """
        >>> ListsHelper.reverse([1, 2, 3])
        [3, 2, 1]
        """
        if collection is None:
            return None
        return [collection[len(collection) - i - 1] for i in range(0, len(collection))]

    @classmethod
    def take(cls, n, iterable):
        import itertools
        return list(itertools.islice(iterable, n))

    @classmethod
    def mean(cls, collection):
        return sum(collection) / len(collection)
