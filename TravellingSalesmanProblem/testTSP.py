import unittest
from TSP import *

class TestSolver(unittest.TestCase):

    temp_matrix1 = np.array([[INF, 10, 8, 19, 12],
                            [10, INF, 20, 6, 3],
                            [8, 20, INF, 4, 2],
                            [19, 6, 4, INF, 7],
                            [12, 3, 2, 7, INF]], dtype=np.float)
    cost_matrix = CostMatrix(temp_matrix1)
    tsp = SolverTSP(cost_matrix)

    def test_solver(self):
        self.tsp.solveTSP()
        self.assertEqual(self.tsp.solution, [(1, 3), (3, 4), (4, 5), (5, 2), (2, 1)])