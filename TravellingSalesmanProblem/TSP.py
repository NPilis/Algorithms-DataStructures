import numpy as np
from typing import Tuple

# Forbidden path as infinity
INF = np.inf

class CostMatrix:

    def __init__(self, matrix):
        self.costMatrix = matrix
        self.rowSize, self.colSize = matrix.shape
        self.lowerBound = 0

    def printMatrix(self) -> None:
        print(self.costMatrix)

    def getLowerBound(self) -> float:
        return self.lowerBound

    # Checks if zero is present minimum once in every column and every row
    def checkForZeros(self) -> bool:

        for r in range(self.rowSize):
            assert_zero_row = False
            assert_zero_col = False
            for c in range(self.colSize):
                if self.costMatrix[r][c] == 0:
                    assert_zero_row = True

                if self.costMatrix[c][r] == 0:
                    assert_zero_col = True

            if assert_zero_col == False or assert_zero_row == False:
                return False

        return True

    # Both functions finds minimum of each row/column, reduces their values and sums for the lowest path length
    def reduceRows(self) -> None:

        row_minimas = self.costMatrix.min(axis=1)
        self.costMatrix = self.costMatrix - np.vstack(row_minimas)
        self.lowerBound += sum(row_minimas)

    def reduceCols(self) -> None:

        col_minimas = self.costMatrix.min(axis=0)
        self.costMatrix = self.costMatrix - col_minimas
        self.lowerBound += sum(col_minimas)

    # Functions find minimum in each row or each column except pair values
    def findMinimumInRow(self, row, col) -> Tuple[int, float]:
        min = self.costMatrix[row][0]
        idx = 0

        for c in range(1, self.colSize):
            if c == col:
                continue
            if self.costMatrix[row][c] < min:
                min = self.costMatrix[row][c]
                idx = c

        return idx, min

    def findMinimumInCol(self, row, col) -> Tuple[int, float]:
        min = self.costMatrix[0][col]
        idx = 0

        for r in range(1, self.colSize):
            if r == row:
                continue
            if self.costMatrix[r][col] < min:
                min = self.costMatrix[r][col]
                idx = r

        return idx, min

    # Function finds pairs of indexes in reduced matrix that has 0 in cell
    def findPairsWithZero(self):

        pairs_indexes = []

        for r in range(self.rowSize):
            for c in range(self.colSize):
                if self.costMatrix[r][c] == 0:
                    pairs_indexes.append((r, c))

        return pairs_indexes

    # Removes row and column at indexes and blocks reverse way
    def deleteAndBan(self,row,col):

        self.costMatrix[col][row] = INF
        self.costMatrix = np.delete(self.costMatrix,row,0)
        self.costMatrix = np.delete(self.costMatrix,col,1)


class TSP_Solver:

    def __init__(self):
        self.solution = []


testMatrix = np.array([[0, 10, 8, 19, 12],
                       [10, 0, 20, 6, 3],
                       [8, 20, 0, 4, 2],
                       [19, 6, 4, 0, 7],
                       [12, 3, 2, 7, 0]], dtype=np.float)

np.fill_diagonal(testMatrix, INF)