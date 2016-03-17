# -*- coding: utf-8 -*-


class Color:
    BLACK = ""
    RED = ""
    BLUE = ""
    GREEN = ""


def progressBar2(current, maxWidth=80, stepSize=10, fillChar="█"):
    numberOfCharsToDisplay = (current * maxWidth) // 100
    print("\r" + "".join(numberOfCharsToDisplay * [fillChar]) + 
          "".join((maxWidth - numberOfCharsToDisplay) * [" "]) + "| " + str(current) + "%", end="")
    if (current == 100):
        print("")


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    import time
    for i in range(1, 11):
        progressBar2(i * 10)
        time.sleep(.1)
    print_format_table()