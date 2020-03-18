import numpy as np

"""
Given a list of cities and the distances between each pair of cities, 
what is the shortest possible route that visits each city and returns 
to the origin city

Little Algorithm approach
"""

# Forbidden path as infinity
INF = np.inf

class CostMatrix:

    def __init__(self, matrix):
        self.cost_matrix = matrix
        self.row_size, self.col_size = matrix.shape
        self.lower_bound = 0
        self.row_map = {i: i+1 for i in range(self.row_size)}
        self.col_map = {i: i+1 for i in range(self.col_size)}

    def printMatrix(self):
        print(self.cost_matrix)

    # Returns the lowest cost of travel
    def getLowerBound(self) -> float:
        return self.lower_bound

    # Checks if zero is present minimum once in every column and every row
    def checkForZeros(self) -> bool:

        for r in range(self.row_size):
            assert_zero_row = False
            assert_zero_col = False
            for c in range(self.col_size):
                if self.cost_matrix[r][c] == 0:
                    assert_zero_row = True

                if self.cost_matrix[c][r] == 0:
                    assert_zero_col = True

            if assert_zero_col is False or assert_zero_row is False:
                return False

        return True

    # Both functions finds minimum of each row/column, reduces their values and sums for the lowest path length
    def reduceRows(self) -> None:

        row_minimas = self.cost_matrix.min(axis=1)
        self.cost_matrix = self.cost_matrix - np.vstack(row_minimas)
        self.lower_bound += sum(row_minimas)

    def reduceCols(self) -> None:

        col_minimas = self.cost_matrix.min(axis=0)
        self.cost_matrix = self.cost_matrix - col_minimas
        self.lower_bound += sum(col_minimas)

    # Functions find minimum in each row or each column except pair values
    def findMinimumInRow(self, row, col) -> float:
        if col == 0:
            min = self.cost_matrix[row][1]
        else:
            min = self.cost_matrix[row][0]

        for c in range(1, self.col_size):
            if c == col:
                continue
            if self.cost_matrix[row][c] < min:
                min = self.cost_matrix[row][c]

        return min

    def findMinimumInCol(self, row, col) -> float:
        if row == 0:
            min = self.cost_matrix[1][col]
        else:
            min = self.cost_matrix[0][col]

        for r in range(1, self.row_size):
            if r == row:
                continue
            if self.cost_matrix[r][col] < min:
                min = self.cost_matrix[r][col]

        return min

    # Function finds pairs of indexes in reduced matrix that has 0 in cell
    def findPairsWithZero(self):

        pairs_indexes = []

        for r in range(self.row_size):
            for c in range(self.col_size):
                if self.cost_matrix[r][c] == 0:
                    pairs_indexes.append((r, c))

        return pairs_indexes

    # Removes row and column at indexes and blocks reverse way if there is any
    def deleteAndBan(self,row,col):

        if self.row_map[row] in self.col_map.values() and self.col_map[col] in self.row_map.values():
            self.cost_matrix[col][row] = INF

        self.cost_matrix = np.delete(self.cost_matrix, row, 0)
        self.cost_matrix = np.delete(self.cost_matrix, col, 1)

    # Modifies mapping when the column or row is deleted 1 -> 0 etc.
    def modifyMapping(self,row,col):

        for i in range(row, self.row_size-1):
            self.row_map[i] = self.row_map[i+1]

        for j in range(col, self.col_size-1):
            self.col_map[j] = self.col_map[j+1]

        del self.row_map[self.row_size - 1]
        del self.col_map[self.col_size - 1]


class SolverTSP:

    def __init__(self,cost_matrix):
        self.cost_matrix = cost_matrix
        self.solution = []
        self.cost = 0
        self.iteration_count = self.cost_matrix.row_size

    # Function search for pair indexes with maximum sum of row an col minimum and adds to solution
    def findNextPath(self):

        pair_indexes = self.cost_matrix.findPairsWithZero()
        temp_sum = 0
        max_sum_idx = 0

        for idx, pair in enumerate(pair_indexes):
            row_min = self.cost_matrix.findMinimumInRow(pair[0],pair[1])
            col_min = self.cost_matrix.findMinimumInCol(pair[0],pair[1])
            if row_min + col_min > temp_sum:
                temp_sum = row_min + col_min
                max_sum_idx = idx

        return pair_indexes[max_sum_idx]

    # Adds pair to solution
    def addToSolution(self, node_pair):
        self.solution.append((self.cost_matrix.row_map[node_pair[0]], self.cost_matrix.col_map[node_pair[1]]))

    # Reducing sizes as rows and columns are deleted
    def reduceSizes(self):
        self.cost_matrix.row_size -= 1
        self.cost_matrix.col_size -= 1
        self.iteration_count -= 1

    # Organizes solution as a path
    def organizeSolution(self):

        organized_solution = [self.solution.pop(0)]
        head = organized_solution[0][0]
        tail = organized_solution[0][1]

        while head != tail:
            for idx, val in enumerate(self.solution):
                if val[0] == tail:
                    organized_solution.append(self.solution.pop(idx))
                    tail = val[1]
                    break

        self.solution = organized_solution

    # All function combined solves the problem
    def solveTSP(self):

        while self.iteration_count > 1:

            if self.cost_matrix.checkForZeros():

                pair = self.findNextPath()
                self.addToSolution(pair)
                self.cost_matrix.deleteAndBan(pair[0], pair[1])
                self.cost_matrix.modifyMapping(pair[0], pair[1])
                self.reduceSizes()

            else:
                self.cost_matrix.reduceRows()
                self.cost_matrix.reduceCols()

        self.solution.append((self.cost_matrix.row_map[0], self.cost_matrix.col_map[0]))
        self.organizeSolution()
        self.cost = self.cost_matrix.lower_bound



