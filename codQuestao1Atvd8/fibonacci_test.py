import unittest
from fibonacci import fib

class TestFibonacci(unittest.TestCase):
    
    def test_fib_base_cases(self):
        # Teste para os casos base
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_fib_general_cases(self):
        # Teste para casos gerais
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)

if __name__ == "__main__":
    unittest.main()