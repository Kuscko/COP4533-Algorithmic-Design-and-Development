import unittest
import timeit

# Test all functions of a python list
class TestPythonListFunctions(unittest.TestCase):

    def setUp(self):
        self.test_list = [1, 2, 3, 4, 5]

    def test_append(self):
        time_taken = timeit.timeit(lambda: self.test_list.append(6), number=995)
        print(f"test_append: {time_taken}")
        self.assertEqual(len(self.test_list), 1000)

    def test_extend(self):
        time_taken = timeit.timeit(lambda: self.test_list.extend([6, 7]), number=1)
        print(f"test_extend: {time_taken}")
        self.assertEqual(self.test_list, [1, 2, 3, 4, 5, 6, 7])

    def test_insert(self):
        time_taken = timeit.timeit(lambda: self.test_list.insert(2, 99), number=1)
        print(f"test_insert: {time_taken}")
        self.assertEqual(self.test_list, [1, 2, 99, 3, 4, 5])

    def test_remove(self):
        time_taken = timeit.timeit(lambda: self.test_list.remove(3), number=1)
        print(f"test_remove: {time_taken}")
        self.assertEqual(self.test_list, [1, 2, 4, 5])

    def test_pop(self):
        popped = self.test_list.pop()
        time_taken = timeit.timeit(lambda: self.test_list.pop(), number=1)
        print(f"test_pop: {time_taken}")
        self.assertEqual(popped, 5)
        self.assertEqual(self.test_list, [1, 2, 3])

    def test_clear(self):
        time_taken = timeit.timeit(lambda: self.test_list.clear(), number=1)
        print(f"test_clear: {time_taken}")
        self.assertEqual(self.test_list, [])

    def test_index(self):
        time_taken = timeit.timeit(lambda: self.test_list.index(3), number=1)
        index = self.test_list.index(3)
        print(f"test_index: {time_taken}")
        self.assertEqual(index, 2)

    def test_count(self):
        time_taken = timeit.timeit(lambda: self.test_list.count(3), number=1)
        print(f"test_count: {time_taken}")
        count = self.test_list.count(3)
        self.assertEqual(count, 1)

    def test_sort(self):
        unsorted_list = [3, 1, 4, 2, 5]
        unsorted_list.sort()
        self.assertEqual(unsorted_list, [1, 2, 3, 4, 5])

    def test_reverse(self):
        self.test_list.reverse()
        self.assertEqual(self.test_list, [5, 4, 3, 2, 1])

    def test_copy(self):
        copied_list = self.test_list.copy()
        self.assertEqual(copied_list, [1, 2, 3, 4, 5])
        self.assertIsNot(copied_list, self.test_list)

if __name__ == '__main__':
    unittest.main()
