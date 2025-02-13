import unittest
import timeit
from custom_linkedlist import LinkedList  # Adjusted import statement

class TestLinkedList(unittest.TestCase):
    ll_timings = {}

    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

    def benchmark(self, func, number=1000):
        timings = []
        for _ in range(5):  # Run 5 times
            self.setUp()
            time_taken = timeit.timeit(func, globals=globals(), number=number)
            timings.append(time_taken)
        average_time = sum(timings) / len(timings)
        return timings, average_time

    def test_ll_append(self):
        timings, average_time = self.benchmark(lambda: self.ll.append(4))
        self.ll_timings['test_ll_append'] = (timings, average_time)
        self.ll.append(4)
        self.assertEqual(self.ll.tail.data, 4)

    def test_ll_getitem(self):
        timings, average_time = self.benchmark(lambda: self.ll[0])
        self.ll_timings['test_ll_getitem'] = (timings, average_time)
        self.assertEqual(self.ll[0], 1)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 3)

    def test_ll_setitem(self):
        timings, average_time = self.benchmark(lambda: setattr(self.ll, '1', 5))
        self.ll_timings['test_ll_setitem'] = (timings, average_time)
        self.ll[1] = 5
        self.assertEqual(self.ll[1], 5)

    def test_ll_delitem(self):
        def del_item():
            print(len(self.ll))
            del self.ll[1]
        timings, average_time = self.benchmark(del_item, number=1)
        self.ll_timings['test_ll_delitem'] = (timings, average_time)
        self.assertEqual(len(self.ll), 3)

    def test_ll_iter(self):
        timings, average_time = self.benchmark(lambda: [item for item in self.ll])
        self.ll_timings['test_ll_iter'] = (timings, average_time)
        items = [item for item in self.ll]
        self.assertEqual(items, [1, 2, 3])

    def test_ll_contains(self):
        timings, average_time = self.benchmark(lambda: 1 in self.ll)
        self.ll_timings['test_ll_contains (1 in ll)'] = (timings, average_time)
        self.assertTrue(1 in self.ll)
        timings, average_time = self.benchmark(lambda: 4 in self.ll)
        self.ll_timings['test_ll_contains (4 not in ll)'] = (timings, average_time)
        self.assertFalse(4 in self.ll)

    def test_ll_pop(self):
        for i in range(1000):
            self.ll.append(i)
        timings, average_time = self.benchmark(lambda: self.ll.pop(), 1)
        self.ll_timings['test_ll_pop'] = (timings, average_time)
        self.ll.pop()
        self.assertEqual(self.ll.tail.data, 1)

    def test_ll_pop_at_index(self):
        timings, average_time = self.benchmark(lambda: self.ll.pop_at_index(1))
        self.ll_timings['test_ll_pop_at_index'] = (timings, average_time)
        self.ll.pop_at_index(1)
        self.assertEqual(self.ll[1], 2)

    def test_ll_insert(self):
        timings, average_time = self.benchmark(lambda: self.ll.insert(1, 4))
        self.ll_timings['test_ll_insert'] = (timings, average_time)
        self.ll.insert(1, 4)
        self.assertEqual(self.ll[1], 4)

    def test_ll_reverse(self):
        timings, average_time = self.benchmark(lambda: self.ll.reverse())
        self.ll_timings['test_ll_reverse'] = (timings, average_time)
        self.ll.reverse()
        self.assertEqual(self.ll[0], 3)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 1)

    def test_ll_extend(self):
        other = LinkedList()
        other.append(4)
        other.append(5)
        timings, average_time = self.benchmark(lambda: self.ll.extend(other))
        self.ll_timings['test_ll_extend'] = (timings, average_time)
        self.ll.extend(other)
        self.assertEqual(self.ll[3], 4)
        self.assertEqual(self.ll[4], 5)

    def test_ll_clear(self):
        timings, average_time = self.benchmark(lambda: self.ll.clear())
        self.ll_timings['test_ll_clear'] = (timings, average_time)
        self.ll.clear()
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

if __name__ == '__main__':
    unittest.main()