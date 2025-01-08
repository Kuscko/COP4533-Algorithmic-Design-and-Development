import unittest
import timeit
from python_vs_linked_lists import LinkedList, Node

# add timeit to all tests

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

    def test_ll_append(self):
        time_taken = timeit.timeit(lambda: self.ll.append(4), globals=globals(), number=1000)
        print(f"test_ll_append: {time_taken}")
        self.ll.append(4)
        self.assertEqual(self.ll.tail.data, 4)

    def test_ll_getitem(self):
        time_taken = timeit.timeit(lambda: self.ll[0], globals=globals(), number=1000)
        print(f"test_ll_getitem: {time_taken}")
        self.assertEqual(self.ll[0], 1)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 3)

    def test_ll_setitem(self):
        time_taken = timeit.timeit(lambda: 'self.ll[1] = 5', globals=globals(), number=1000)
        print(f"test_ll_setitem: {time_taken}")
        self.ll[1] = 5
        self.assertEqual(self.ll[1], 5)

    # TODO: re-evaluate this test
    def test_ll_delitem(self):
        def del_item():
            print(self.ll[1])
            del self.ll[1]
            print(self.ll[1])
        time_taken = timeit.timeit(del_item, globals=globals(), number=1)
        print(f"test_ll_delitem: {time_taken}")
        self.assertEqual(len(self.ll), 3)

    def test_ll_iter(self):
        time_taken = timeit.timeit(lambda: [item for item in self.ll], globals=globals(), number=1000)
        print(f"test_ll_iter: {time_taken}")
        items = [item for item in self.ll]
        self.assertEqual(items, [1, 2, 3])

    def test_ll_contains(self):
        time_taken = timeit.timeit(lambda: 1 in self.ll, globals=globals(), number=1000)
        print(f"test_ll_contains (1 in ll): {time_taken}")
        self.assertTrue(1 in self.ll)
        time_taken = timeit.timeit(lambda: 4 in self.ll, globals=globals(), number=1000)
        print(f"test_ll_contains (4 not in ll): {time_taken}")
        self.assertFalse(4 in self.ll)

    def test_ll_pop(self):
        for i in range(1000):
            self.ll.append(i)
        time_taken = timeit.timeit(lambda: self.ll.pop(), globals=globals(), number=1000)
        print(f"test_ll_pop: {time_taken}")
        self.ll.pop()
        self.assertEqual(self.ll.tail.data, 2)

    def test_ll_pop_at_index(self):
        time_taken = timeit.timeit(lambda: self.ll.pop_at_index(1), globals=globals(), number=1000)
        print(f"test_ll_pop_at_index: {time_taken}")
        self.ll.pop_at_index(1)
        self.assertEqual(self.ll[1], 2)

    def test_ll_insert(self):
        time_taken = timeit.timeit(lambda: self.ll.insert(1, 4), globals=globals(), number=1000)
        print(f"test_ll_insert: {time_taken}")
        self.ll.insert(1, 4)
        self.assertEqual(self.ll[1], 4)

    def test_ll_reverse(self):
        time_taken = timeit.timeit(lambda: self.ll.reverse(), globals=globals(), number=1000)
        print(f"test_ll_reverse: {time_taken}")
        self.ll.reverse()
        self.assertEqual(self.ll[0], 3)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 1)

    def test_ll_extend(self):
        other = LinkedList()
        other.append(4)
        other.append(5)
        time_taken = timeit.timeit(lambda: self.ll.extend(other), globals=globals(), number=1000)
        print(f"test_ll_extend: {time_taken}")
        self.ll.extend(other)
        self.assertEqual(self.ll[3], 4)
        self.assertEqual(self.ll[4], 5)

    def test_ll_clear(self):
        time_taken = timeit.timeit(lambda: self.ll.clear(), globals=globals(), number=1000)
        print(f"test_ll_clear: {time_taken}")
        self.ll.clear()
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

if __name__ == '__main__':
    unittest.main()