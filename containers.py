

###
# Stack container based on a list for its internal storage
#
class Stack:
    def __init__(self):
        self.internal_list = list()

    def isEmpty(self):
        """
        >>> s.isEmpty()
        True
        """
        return len(self.internal_list) == 0

    def pop(self):
        """
        >>> s.pop()
        """
        return self.internal_list.pop() if self.internal_list else None

    def push(self, element):
        """
        >>> s.push(1)
        >>> s.push(2)
        """
        self.internal_list.append(element)

    def top(self):
        """
        >>> s.top()
        2
        """
        return self.internal_list[-1]

    def print_content(self):
        print("+---------+")
        for i in range(len(self.internal_list)):
            print("   " + str(self.internal_list[len(self.internal_list) - 1 - i]))
            print("+---------+")

    def size(self):
        """
        >>> s.size()
        2
        """
        return len(self.internal_list)


class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def addChild(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.addChild(node)
        elif node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.addChild(node)


def flatten(lst):
    """
    >>> flatten([[[1],2,[3,4]],5,[6],[7,8,9]])
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
        >>> uniq([1,1,1,2,2,3,3,4,4,4,4,4,4,5,6,7,7,7,7,7,8,9])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> uniq((1,1,1,2,2,3,3,4,4,4,4,4,4,5,6,7,7,7,7,7,8,9))
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> uniq(['a','z','a','b','a','z','b'])
        ['a', 'z', 'b']
    """
    return list(set(array))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False, extraglobs={'s': Stack()})
