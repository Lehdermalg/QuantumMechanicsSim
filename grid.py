import numpy as np


class Grid(object):
    def __init__(self, n: int, z: float):
        self.n = n  # amount of points
        self.z = z  # first element
        self.d = -self.z / (self.n/2-1)
        self.space = np.linspace(self.z, -self.z + self.d, self.n)

    @property
    def mid_space(self):
        return self.space[self.n//2-1]

    def shift_up(self):
        m = -self.space[0]
        self.space += m

    def shift_down(self):
        m = -self.space[-1]
        self.space += m
