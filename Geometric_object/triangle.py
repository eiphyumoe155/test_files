import pandas as pd
import numpy as np
import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def perimeter(self):
        return (self.s1 + self.s2 + self.s3)
    
    def pythagoras(self):
        return (math.sqrt(self.s1 ** 2 + self.s2 ** 2))
    
    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        area = s * (s - self.s1) * (s - self.s2) * (s - self.s3)
        return area**0.5
