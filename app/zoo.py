"""
Zoo of lifeforms for Conway's Game of Life

Created by Tom Callahan
2/1/2019
"""
import csv
class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.zoo = []
    
    def add(self, lifeform):
        """ Add a given lifeform to a zoo """
        lifeform_exists = False
        for idx, lf in enumerate(self.zoo):
            if lf.label == lifeform.label:
                lifeform_exists = True
                self.zoo[idx] = lifeform
        if lifeform_exists == False:
            self.zoo.append(lifeform)

    def remove(self, label):
        """ Remove a lifeform with a given label from a zoo """
        for idx, lf in enumerate(self.zoo):
            if lf.label == label:
                del self.zoo[idx]

    def get(self, label):
        """ Return a lifeform with a given label from a zoo """
        resp = {}
        for idx, lf in enumerate(self.zoo):
            if lf.label == label:
                resp = {"label": lf.label, 
                        "cells": lf.cells, 
                        "width": lf.width}
        return resp

    def lst(self):
        """ Returns a list of the labels of zoo lifeforms """
        return [lifeform.label for lifeform in self.zoo]


class Lifeform(object):
    def __init__(self, label, cells, width):
        self.label = label
        self.cells = cells
        self.width = width


def load_zoo(store):
    z = Zoo("default")
    with open(store,'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for label, cells, width in reader:
            z.add(Lifeform(label, cells, width))
    return z

def save_zoo(store):
    pass

            