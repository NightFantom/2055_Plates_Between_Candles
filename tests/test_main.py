from unittest import TestCase

from main import Solution


class TestSolution(TestCase):

    def test_1(self):
        table = "**|**|***|"
        queries = [[2, 5], [5, 9]]
        expected = [2, 3]
        result = Solution().platesBetweenCandles(table, queries)
        self.assertListEqual(expected, result)

    def test_2(self):
        table = "***|**|*****|**||**|*"
        queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        expected = [9, 0, 0, 0, 0]
        result = Solution().platesBetweenCandles(table, queries)
        self.assertListEqual(expected, result)

    def test_3(self):
        table = "*|" * (5 * 10 ^ 4)
        queries = []
        expected = []
        for i in range(len(table) - 3):
            queries.append([i, i + 3])
            expected.append(1)
        result = Solution().platesBetweenCandles(table, queries)
        self.assertListEqual(expected, result)

    def test_4(self):
        table = "*|*||||**|||||||*||*||*||**|*|*||*"
        queries = [[2, 33], [2, 32], [3, 31], [0, 33], [1, 24], [3, 20], [7, 11], [5, 32], [2, 31], [5, 31], [0, 31],
                   [3, 28], [4, 33], [6, 29], [2, 30], [2, 28], [1, 30], [1, 33], [4, 32], [5, 30], [4, 23], [0, 30],
                   [3, 10], [5, 28], [0, 28], [4, 28], [3, 33], [0, 27]]
        expected = [9, 9, 9, 10, 6, 4, 0, 9, 9, 9, 10, 7, 9, 8, 8, 7, 9, 10, 9, 8, 5, 9, 2, 7, 8, 7, 9, 8]
        result = Solution().platesBetweenCandles(table, queries)
        self.assertListEqual(expected, result)

    def test_5(self):
        table = "*|*"
        queries = [[2,2]]
        expected = [0]
        result = Solution().platesBetweenCandles(table, queries)
        self.assertListEqual(expected, result)