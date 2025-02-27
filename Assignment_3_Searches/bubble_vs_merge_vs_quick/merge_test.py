import timeit
from merge_string_list import MergeStringList

def test_merge():
    merge_list = MergeStringList()
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
               "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    
    for s in strings:
        merge_list.add(s)
    
    # Test sorting
    time_sort = timeit.timeit(lambda: merge_list.sort(), number=1)
    print(f"Merge Sort: {time_sort:.10f} seconds")

if __name__ == "__main__":
    test_merge()