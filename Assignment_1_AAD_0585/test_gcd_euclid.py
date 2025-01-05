import unittest
from timeit import timeit
from assignment_1_gcd_euclid import gcd_euclid

# FILE: test_gcd_euclid.py


class TestGCDEuclid(unittest.TestCase):
    def test_gcd_euclid(self):
        # Test cases with known inputs and expected outputs
        self.assertEqual(gcd_euclid(48, 18), 6)
        self.assertEqual(gcd_euclid(56, 98), 14)
        self.assertEqual(gcd_euclid(101, 103), 1)
        self.assertEqual(gcd_euclid(0, 5), 5)
        self.assertEqual(gcd_euclid(5, 0), 5)
        self.assertEqual(gcd_euclid(0, 0), 0)

    def test_performance(self):
        # Measure performance using timeit
        print("Performance test for gcd_euclid")
        time_taken = timeit("gcd_euclid(48, 18)", globals=globals(), number=1000)
        print(f"Time taken for 1000 iterations of gcd_euclid(48, 18): {time_taken} seconds")

if __name__ == '__main__':
    unittest.main()