import unittest
from TSP import *

class TestSolver(unittest.TestCase):

    def setUp(self):
        self.tempMatrix = np.array([[INF, 10, 8, 19, 12],
                           [10, INF, 20, 6, 3],
                           [8, 20, INF, 4, 2],
                           [19, 6, 4, INF, 7],
                           [12, 3, 2, 7, INF]], dtype=np.float)
        self.costMatrix = CostMatrix(self.tempMatrix)
        self.tsp = TSP_Solver(self.costMatrix)

    def test_print(self):
        self.tsp.costMatrix.printMatrix()

    def test_solver(self):
        self.tsp.solveTSP()
        self.tsp.costMatrix.printMatrix()
        print(self.tsp.solution)