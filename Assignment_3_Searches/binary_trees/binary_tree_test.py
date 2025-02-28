import timeit
from binary_tree_string_list import BinaryTreeStringList

def test_binary_tree():
    bt_list = BinaryTreeStringList()
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
               "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    
    for s in strings:
        bt_list.add(s)
    
    # Test finding an existing word
    time_existing = timeit.timeit(lambda: bt_list.find("kiwi"), number=1000)
    print(f"Binary Tree Search (existing): {time_existing:.10f} seconds")
    
    # Test finding a non-existing word
    time_non_existing = timeit.timeit(lambda: bt_list.find("blueberry"), number=1000)
    print(f"Binary Tree Search (non-existing): {time_non_existing:.10f} seconds")

if __name__ == "__main__":
    test_binary_tree()