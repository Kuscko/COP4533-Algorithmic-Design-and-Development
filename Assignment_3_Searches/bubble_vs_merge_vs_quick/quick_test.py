import timeit
from quick_string_list import QuickStringList

def test_quick():
    quick_list = QuickStringList()
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
               "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    
    for s in strings:
        quick_list.add(s)
    
    # Test sorting
    time_sort = timeit.timeit(lambda: quick_list.sort(), number=1)
    print(f"Quick Sort: {time_sort:.10f} seconds")

if __name__ == "__main__":
    test_quick()