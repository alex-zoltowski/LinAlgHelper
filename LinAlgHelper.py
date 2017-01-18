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

    def get_leading_num(self, row):
        return self.matrix[row][self.get_leading_col(row)]

    def floats_to_ints(self):
        for i in range(self.rows):
            for x in range(self.cols):
                if float(self.matrix[i][x]).is_integer():
                    self.matrix[i][x] = int(self.matrix[i][x])

    def print_matrix(self):
        print('\n'.join([''.join(['{:5}'.format(item) for item in row])
            for row in self.matrix]))

        print('----------------------')

    def swap(self, row1, row2):
        for i in range(self.cols):
            num1 = self.matrix[row1][i]
            num2 = self.matrix[row2][i]
            self.matrix[row1][i] = num2
            self.matrix[row2][i] = num1

        self.print_matrix()

    def replace(self, change_row, base_row):
        factor = (self.matrix[change_row][self.get_leading_col(change_row)] * -1) \
                    / (self.matrix[base_row][self.get_leading_col(base_row)])
        for i in range(self.cols):
            self.matrix[change_row][i] += factor * self.matrix[base_row][i]

        self.floats_to_ints()
        self.print_matrix()

    def scale(self):
        for row in range(self.rows):
            if self.get_leading_num(row) < 1.0 and\
                    self.get_leading_num(row) > -1.0:
                divisor = self.get_leading_num(row)
            elif self.get_leading_num(row) == 0 or\
                    self.get_leading_num(row) == 1:
                continue
            else:
                divisor = abs(reduce(lambda x,y: gcd(x, y), self.matrix[row]))
                if self.get_leading_num(row) < 0:
                    divisor *= -1

            for i in range(self.cols):
                self.matrix[row][i] /= divisor

        self.floats_to_ints()
        self.print_matrix()

    def get_echelon_form(self):
        matrix = self.matrix
        matrix.scale()
        working_column = 0
        # for i in range(self.rows):
        #     if matrix[i][working_column] == 1 and i < :

        return matrix



matrix = AugmentedMatrix()

matrix.set_val(0, 0, 1)
matrix.set_val(0, 1, 2)
matrix.set_val(0, 2, 4)
matrix.set_val(0, 3, 2)
matrix.set_val(1, 0, 0)
matrix.set_val(1, 1, -6)
matrix.set_val(1, 2, 2)
matrix.set_val(1, 3, 4)
matrix.print_matrix()
matrix.scale()
# matrix.set_val(2, 0, 4)
# matrix.set_val(2, 1, -8)
# matrix.set_val(2, 2, 12)
# matrix.set_val(2, 3, 1)
#
# matrix.print_matrix()
# matrix.swap(0, 1)
# matrix.replace(2, 0)
