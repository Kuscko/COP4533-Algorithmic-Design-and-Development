import timeit
from binary_string_list import BinaryStringList

def test_binary():
    bin_list = BinaryStringList()
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
               "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    
    for s in strings:
        bin_list.add(s)
    
    # Test finding an existing word
    time_existing = timeit.timeit(lambda: bin_list.find("kiwi"), number=1000)
    print(f"Binary Search (existing): {time_existing:.10f} seconds")
    
    # Test finding a non-existing word
    time_non_existing = timeit.timeit(lambda: bin_list.find("blueberry"), number=1000)
    print(f"Binary Search (non-existing): {time_non_existing:.10f} seconds")

if __name__ == "__main__":
    test_binary()