import os
import timeit
import unittest
from html_search_regex_ver import check_html
from html_search_stack_ver import check_html_tags


class TestHtmlSearch(unittest.TestCase):
    def setUp(self):
        self.test_file = os.path.join(os.path.dirname(__file__), "index.html")

    def test_html_search_with_regex(self):
        timings = []
        for _ in range(5):  # Run 5 times
            start_time = timeit.default_timer()
            valid_check = check_html(self.test_file)
            end_time = timeit.default_timer()
            timings.append(end_time - start_time)
        
        for i, timing in enumerate(timings, 1):
            print(f"Run {i}: {timing:.6f} seconds | Result: {valid_check}")
        
        average_time = sum(timings) / len(timings)
        print(f"\nAverage Time: {average_time:.6f} seconds")

    def test_html_search_with_stack(self):
        timings = []
        for _ in range(5):  # Run 5 times
            start_time = timeit.default_timer()
            valid_check = check_html_tags(self.test_file)
            end_time = timeit.default_timer()
            timings.append(end_time - start_time)
        
        for i, timing in enumerate(timings, 1):
            print(f"Run {i}: {timing:.6f} seconds | Result: {valid_check}")
        
        average_time = sum(timings) / len(timings)
        print(f"\nAverage Time: {average_time:.6f} seconds")


if __name__ == "__main__":
    unittest.main()