#!/usr/bin/python3
# -*- coding: utf-8 -*-


class ProgressBar:
    """
    >>> helper = ProgressBar()
    >>> helper.set_width(80)
    >>> helper.get_width()
    80
    >>> helper.advance(10)
    \r|=======>                                                                        | 10%
    >>> helper.advance(90)
    \r|===============================================================================>| 100%
    """
    def __init__(self, bar_width=80, filled_char="=", empty_char=" "):
        self.bar_width = bar_width
        self.filled_char = filled_char
        self.empty_char = empty_char
        self.progress = 0

    def set_width(self, width):
        self.bar_width = width

    def get_width(self):
        return self.bar_width

    def advance(self, step=1):
        if self.progress < 100:
            self.progress += step
            self.render()

    def render(self):
        normalized_progress = (self.progress * self.bar_width) // 100
        print("\r|" + "".join((normalized_progress-1) * [self.filled_char]) + ">" +
              "".join((self.bar_width - normalized_progress) * [self.empty_char]) + "| " +
              str(self.progress) + "%", end="")

        if self.progress == 100:
            print("")
