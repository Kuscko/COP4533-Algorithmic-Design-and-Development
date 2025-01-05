import unittest
from timeit import timeit
from assignment_1_gcd_math import gcd_math

# FILE: test_gcd_math.py


class TestGCDMath(unittest.TestCase):
    def test_gcd_math(self):
        # Test cases with known inputs and expected outputs
        self.assertEqual(gcd_math(48, 18), 6)
        self.assertEqual(gcd_math(56, 98), 14)
        self.assertEqual(gcd_math(101, 103), 1)
        self.assertEqual(gcd_math(0, 5), 5)
        self.assertEqual(gcd_math(5, 0), 5)
        self.assertEqual(gcd_math(0, 0), 0)

    def test_performance(self):
        # Measure performance using timeit
        print("Performance test for gcd_math")
        time_taken = timeit("gcd_math(48, 18)", globals=globals(), number=1000)
        print(f"Time taken for 1000 iterations of gcd_math(48, 18): {time_taken} seconds")

if __name__ == '__main__':
    unittest.main()