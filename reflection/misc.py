#!/usr/bin/python3
# -*- coding: utf-8 -*-

from inspect import isfunction


def getObjectAttributes(obj):
    if obj is None:
        return None:
    lst = []
    for a in dir(obj):
        if a.startswith("__") is False:
            if isfunction(a) is True:
                continue;
            lst.append(a)
    return lst
    
def getObjectFunctions(obj):
    if obj is None:
        return None
    lst = []
    for a in dir(obj):
        if a.startswith("__") is False:
            if isfunction(a) is True:
                lst.append(a)
    return lst  