import numpy as np
from typing import Tuple

# Forbidden path as infinity
INF = np.inf

class CostMatrix:

    def __init__(self, matrix):
        self.costMatrix = matrix
        self.rowSize, self.colSize = matrix.shape
        self.lowerBound = 0
        self.rowMap = {i:i+1 for i in range(self.rowSize)}
        self.colMap = {i:i+1 for i in range(self.colSize)}

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
    def findMinimumInRow(self, row, col) -> float:
        if col == 0:
            min = self.costMatrix[row][1]
        else:
            min = self.costMatrix[row][0]

        for c in range(1, self.colSize):
            if c == col:
                continue
            if self.costMatrix[row][c] < min:
                min = self.costMatrix[row][c]

        return min

    def findMinimumInCol(self, row, col) -> float:
        if row == 0:
            min = self.costMatrix[1][col]
        else:
            min = self.costMatrix[0][col]

        for r in range(1, self.rowSize):
            if r == row:
                continue
            if self.costMatrix[r][col] < min:
                min = self.costMatrix[r][col]


        return min

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

        if row in self.rowMap.keys():
            if col in self.rowMap.keys():
                self.costMatrix[col][row] = INF

        self.costMatrix = np.delete(self.costMatrix,row,0)
        self.costMatrix = np.delete(self.costMatrix,col,1)

    def modifyMapping(self,row,col):



class TSP_Solver:

    def __init__(self,costMatrix):
        self.costMatrix = costMatrix
        self.solution = []
        self.cost = 0
        self.iterationCount = self.costMatrix.rowSize

    # Function search for pair indexes with maximum sum of row an col minimum and adds to solution
    def findNextPath(self):

        pair_indexes = self.costMatrix.findPairsWithZero()
        temp_sum = 0
        max_sum_idx = 0

        for idx,pair in enumerate(pair_indexes):
            row_min = self.costMatrix.findMinimumInRow(pair[0],pair[1])
            col_min = self.costMatrix.findMinimumInCol(pair[0],pair[1])
            if row_min + col_min > temp_sum:
                temp_sum = row_min + col_min
                max_sum_idx = idx

        return pair_indexes[max_sum_idx]

    def addToSolution(self,node_pair):
        self.solution.append((self.costMatrix.rowMap[node_pair[0]],self.costMatrix.colMap[node_pair[1]]))

    def reduceSizes(self):
        self.costMatrix.rowSize -= 1
        self.costMatrix.colSize -= 1
        self.iterationCount -= 1

    def solveTSP(self):

        while self.iterationCount > 1:
            if self.costMatrix.checkForZeros():
                pair = self.findNextPath()
                self.addToSolution(pair)
                self.costMatrix.deleteAndBan(pair[0],pair[1])
                self.costMatrix.modifyMapping(pair[0],pair[1])
                self.reduceSizes()
            else:
                self.costMatrix.reduceRows()
                self.costMatrix.reduceCols()



tempMatrix = np.array([[INF, 10, 8, 19, 12],
                           [10, INF, 20, 6, 3],
                           [8, 20, INF, 4, 2],
                           [19, 6, 4, INF, 7],
                           [12, 3, 2, 7, INF]], dtype=np.float)
costMatrix = CostMatrix(tempMatrix)
tsp = TSP_Solver(costMatrix)
tsp.solveTSP()
print(tsp.solution)