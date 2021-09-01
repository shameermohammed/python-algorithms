import unittest
import linear_search

class TestLinearSearch(unittest.TestCase):
    
    def test_linear_search(self):
        self.assertEqual(linear_search.linearSearch([1, 2, 3, 4, 4, 5, 6, 7], 4, lambda a,b: a-b), [3, 4])
        self.assertEqual(linear_search.linearSearch([-1, 0, 1], 4, lambda a,b: a-b), [])
        self.assertEqual(linear_search.linearSearch([4, 4, 4], 4, lambda a,b: a-b), [0, 1, 2])
        


if __name__ == "__main__":
    unittest.main()