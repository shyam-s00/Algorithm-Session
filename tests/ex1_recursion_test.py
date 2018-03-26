import unittest
from ex1_recursion import factorial

class factorial_test(unittest.TestCase):

    def test_fact(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        #self.assertEqual(factorial(-1), None)

if __name__ == '__main__':
    unittest.main()