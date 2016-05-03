#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math

class TableHelper:
    def __init__(self, width=80):
        self.width = width
        self.headers = []

    def add_column(self, title):
        self.headers.append(title)

    def display(self):
        pass

    def print_header(self):
        column_width = ((self.width ) / len(self.headers))
        print(column_width)
        column_width = int(column_width)
        print("+" + str((self.width) * "-") + "+")
        for header in self.headers:
            print("|" + header.center(column_width), end='')
        print("|")
        print("+" + str((self.width) * "-") + "+")


if __name__ == "__main__":
    helper = TableHelper(80)
    helper.add_column("Name")
    helper.add_column("Last name")

    helper.add_column("Age")
    helper.print_header()