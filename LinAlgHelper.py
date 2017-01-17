#!/usr/bin/python
from __future__ import division
from fractions import gcd
from functools import reduce

class AugmentedMatrix():

    def __init__(self):
        self.cols = int(input('Cols: '))
        self.rows = int(input('Rows: '))
        self.matrix = [[0 for x in range(int(self.cols))] for y in range(int(self.rows))]

    def set_val(self, row, col, val):
        self.matrix[row][col] = val

    def get_leading_col(self, row):
        for i in range(self.cols):
            if self.matrix[row][i] != 0:
                return i
                break

        return 0

    def print_matrix(self):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
            for row in self.matrix]))

        print('----------------------')

    def swap(self, row1, row2):
        for i in range(self.cols):
            self.matrix[row1][i] = self.matrix[row2][i]
            self.matrix[row2][i] = self.matrix[row1][i]

        self.print_matrix()

    def replace(self, change_row, base_row):
        factor = self.matrix[change_row][self.get_leading_col(change_row)] * -1
        for i in range(self.cols):
            self.matrix[change_row][i] += factor * self.matrix[base_row][i]

        self.print_matrix()

    def scale(self):
        for row in range(self.rows):
            divisor = reduce(lambda x,y: gcd(x, y), self.matrix[row])
            if divisor != 1 and len(set(self.matrix[row])) > 2:
                print(divisor)
                for i in range(self.cols):
                    print(self.matrix[row][i])
                    self.matrix[row][i] /= divisor
            if len(set(self.matrix[row])) == 2:
                for i in range(self.cols):
                    if self.matrix[row][i] != 0:
                        self.matrix[row][i] = 1

            self.print_matrix()


matrix = AugmentedMatrix()
print(-8*(1/2))
matrix.set_val(0, 0, 1)
matrix.set_val(0, 1, -2)
matrix.set_val(0, 2, 1)
matrix.set_val(0, 3, 0)
matrix.set_val(1, 0, 0)
matrix.set_val(1, 1, 2)
matrix.set_val(1, 2, -8)
matrix.set_val(1, 3, 8)
matrix.set_val(2, 0, 5)
matrix.set_val(2, 1, 0)
matrix.set_val(2, 2, -5)
matrix.set_val(2, 3, 10)

matrix.print_matrix()
matrix.replace(2, 0)
matrix.scale()
matrix.replace(2, 1)
matrix.scale()
