"""
Zoo of lifeforms for Conway's Game of Life

Created by Tom Callahan
2/1/2019
"""
class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.zoo = []
    
    def add(self, lifeform):
        lifeform_exists = False
        for idx, lf in enumerate(self.zoo):
            if lf['name'] == lifeform['name']:
                lifeform_exists = True
                self.zoo[idx] = lifeform
        if lifeform_exists == False:
            self.zoo.append(lifeform)

