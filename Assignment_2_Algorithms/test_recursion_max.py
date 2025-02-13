import unittest
import timeit
from recursion_max_sorting import find_max as find_max_sorting
from recursion_max_unsorted_cases import find_max as find_max_unsorted_cases

class TestFinxMax(unittest.TestCase):
    def test_find_max_sorting(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [-5, -2, -1, -3],
            [10, 5, 15, 20, 25],
            [42],
            []
        ]
        timings = []
        for _ in range(5):  # Run 5 times for each test case
            start_time = timeit.default_timer()
            for case in test_cases:
                try:
                    find_max_sorting(case)
                except ValueError:
                    pass
            end_time = timeit.default_timer()
            timings.append(end_time - start_time)

        print("Find Max Sorting")
        for i, timing in enumerate(timings, 1):
            print(f"Run {i}: {timing:.6f} seconds")
        
        average_time = sum(timings) / len(timings)
        print(f"\nAverage Time: {average_time:.6f} seconds")

    def test_find_max_unsorted_cases(self):
        test_cases = [
            [1, 2, 3, 4, 5],
            [-5, -2, -1, -3],
            [10, 5, 15, 20, 25],
            [42],
            []
        ]
        timings = []
        for _ in range(5):  # Run 5 times for each test case
            start_time = timeit.default_timer()
            for case in test_cases:
                try:
                    find_max_unsorted_cases(case)
                except ValueError:
                    pass
            end_time = timeit.default_timer()
            timings.append(end_time - start_time)
        
        print("Find Max Unsorted Cases")
        for i, timing in enumerate(timings, 1):
            print(f"Run {i}: {timing:.6f} seconds")
        
        average_time = sum(timings) / len(timings)
        print(f"\nAverage Time: {average_time:.6f} seconds")