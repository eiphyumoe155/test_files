import pandas as pd
import numpy as np
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.pi = 3.14
        self.circumference = 0

    def area(self, radius):
        area = self.pi * np.square(radius)
        return area
    
    def find_radius(self):
        self.radius = self.diameter / 2
        return self.radius
    
    def find_circumference(self):
        self.circumference = 2 * self.pi * self.radius
        return self.circumference

