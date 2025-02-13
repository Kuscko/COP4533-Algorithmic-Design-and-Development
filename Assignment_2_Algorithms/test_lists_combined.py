from test_linked_lists import TestLinkedList
from test_python_lists import TestPythonListFunctions

def print_timings():
    python_list = TestPythonListFunctions()
    python_list.setUp()
    # Run all python_list tests
    python_list.test_append()
    python_list.test_clear()
    python_list.test_count()
    python_list.test_index()
    python_list.test_pop()
    python_list.test_remove()
    python_list.test_sort()
    python_list.test_extend()
    python_list.test_insert()
    python_list.test_reverse()
    python_list.test_copy()
    python_list.test_extend()

    linked_list = TestLinkedList()
    linked_list.setUp()
    linked_list.test_ll_append()
    print(linked_list.ll_timings.items())
    linked_list.test_ll_getitem()
    print(linked_list.ll_timings.items())
    linked_list.test_ll_setitem()
    print(linked_list.ll_timings.items())
    linked_list.test_ll_delitem()
    linked_list.test_ll_iter()
    linked_list.test_ll_contains()
    linked_list.test_ll_pop()
    linked_list.test_ll_pop_at_index()
    linked_list.test_ll_insert()
    linked_list.test_ll_reverse()
    linked_list.test_ll_extend()
    linked_list.test_ll_clear()

    print("\nTimings:")
    print(f"{'Test':<30} {'Python List Timings':<50} {'Linked List Timings':<30}")
    print("="*110)
    all_keys = set(python_list.py_list_timings.keys()).union(set(linked_list.ll_timings.keys()))
    
    total_python_time = 0
    total_linked_time = 0
    count_python = 0
    count_linked = 0
    
    for test_name in all_keys:
        python_time = python_list.py_list_timings.get(test_name, (None, 0))[1]
        linked_time = linked_list.ll_timings.get(test_name, (None, 0))[1]
        
        if python_time:
            total_python_time += python_time
            count_python += 1
        if linked_time:
            total_linked_time += linked_time
            count_linked += 1
        
        print(f"{test_name:<30} {python_time:.10f} seconds{'':<30} {linked_time:.10f} seconds")
    
    avg_python_time = total_python_time / count_python if count_python else 0
    avg_linked_time = total_linked_time / count_linked if count_linked else 0
    
    print("="*110)
    print(f"{'Average':<30} {avg_python_time:.10f} seconds{'':<30} {avg_linked_time:.10f} seconds")


if __name__ == "__main__":
    print_timings()