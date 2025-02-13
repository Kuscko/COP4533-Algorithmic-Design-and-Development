import unittest
import timeit

# Test all functions of a python list
class TestPythonListFunctions(unittest.TestCase):
    py_list_timings = {}

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5]

    def benchmark(self, func, number=1000):
        timings = []
        for _ in range(5):  # Run 5 times
            self.setUp()
            time_taken = timeit.timeit(func, globals=globals(), number=number)
            timings.append(time_taken)
        average_time = sum(timings) / len(timings)
        return timings, average_time

    def test_append(self):
        timings, average_time = self.benchmark(lambda: self.test_list.append(6), number=995)
        self.py_list_timings['test_append'] = (timings, average_time)
        self.assertEqual(len(self.test_list), 1000)

    def test_extend(self):
        timings, average_time = self.benchmark(lambda: self.test_list.extend([6, 7]), number=1)
        self.py_list_timings['test_extend'] = (timings, average_time)
        self.assertEqual(self.test_list, [1, 2, 3, 4, 5, 6, 7])

    def test_insert(self):
        timings, average_time = self.benchmark(lambda: self.test_list.insert(2, 99), number=1)
        self.py_list_timings['test_insert'] = (timings, average_time)
        self.assertEqual(self.test_list, [1, 2, 99, 3, 4, 5])

    def test_remove(self):
        timings, average_time = self.benchmark(lambda: self.test_list.remove(3), number=1)
        self.py_list_timings['test_remove'] = (timings, average_time)
        self.assertEqual(self.test_list, [1, 2, 4, 5])

    def test_pop(self):
        popped = self.test_list.pop()
        timings, average_time = self.benchmark(lambda: self.test_list.pop(), number=1)
        self.py_list_timings['test_pop'] = (timings, average_time)
        self.assertEqual(popped, 5)
        self.assertEqual(self.test_list, [1, 2, 3, 4])

    def test_clear(self):
        timings, average_time = self.benchmark(lambda: self.test_list.clear(), number=1)
        self.py_list_timings['test_clear'] = (timings, average_time)
        self.assertEqual(self.test_list, [])

    def test_index(self):
        timings, average_time = self.benchmark(lambda: self.test_list.index(3), number=1)
        self.py_list_timings['test_index'] = (timings, average_time)
        index = self.test_list.index(3)
        self.assertEqual(index, 2)

    def test_count(self):
        timings, average_time = self.benchmark(lambda: self.test_list.count(3), number=1)
        self.py_list_timings['test_count'] = (timings, average_time)
        count = self.test_list.count(3)
        self.assertEqual(count, 1)

    def test_sort(self):
        unsorted_list = [3, 1, 4, 2, 5]
        timings, average_time = self.benchmark(lambda: unsorted_list.sort(), number=1)
        self.py_list_timings['test_sort'] = (timings, average_time)
        self.assertEqual(unsorted_list, [1, 2, 3, 4, 5])

    def test_reverse(self):
        timings, average_time = self.benchmark(lambda: self.test_list.reverse(), number=1)
        self.py_list_timings['test_reverse'] = (timings, average_time)
        self.assertEqual(self.test_list, [5, 4, 3, 2, 1])

    def test_copy(self):
        timings, average_time = self.benchmark(lambda: self.test_list.copy(), number=1)
        self.py_list_timings['test_copy'] = (timings, average_time)
        copied_list = self.test_list.copy()
        self.assertEqual(copied_list, [1, 2, 3, 4, 5])
        self.assertIsNot(copied_list, self.test_list)

if __name__ == '__main__':
    unittest.main()
