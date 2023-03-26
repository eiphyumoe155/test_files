import numpy as np
import pandas as pd

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        area = self.width * self.height
        return area
    
    def perimeter(self):
        return (2 * self.width + 2 * self.height)