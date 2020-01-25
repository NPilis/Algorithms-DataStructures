import unittest
from InsertionSort import Series

class InsertionSortTest(unittest.TestCase):

    def test_isSortedSB(self):
        s1 = Series([1, 4, 2, 3, 8, 5])
        s1.insertionSortSB()
        self.assertEqual([1,2,3,4,5,8], s1.series)
        self.assertNotEqual([1,2,3,5,4,8], s1.series)

    def test_isSortedBS(self):
        s1 = Series([1, 4, 2, 3, 8, 5])
        s1.insertionSortBS()
        self.assertEqual([8,5,4,3,2,1], s1.series)
        self.assertNotEqual([1, 2, 3, 5, 4, 8], s1.series)

if __name__ == '__main__':
    unittest.main()