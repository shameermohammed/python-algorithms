import unittest
import jump_search

class TestJumpSearch(unittest.TestCase):
    def test_jump_search(self):
        self.assertEqual(jump_search.jumpSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, lambda a,b: a - b), 6)
        self.assertEqual(jump_search.jumpSearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, lambda a,b: a - b), -1)
        self.assertEqual(jump_search.jumpSearch([], 7, lambda a,b: a - b), -1)

if __name__ == "__main__":
    unittest.main()