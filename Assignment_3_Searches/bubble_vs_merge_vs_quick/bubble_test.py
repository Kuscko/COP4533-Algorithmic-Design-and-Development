import timeit
from bubble_string_list import BubbleStringList

def test_bubble():
    bubble_list = BubbleStringList()
    strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
               "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    
    for s in strings:
        bubble_list.add(s)
    
    # Test sorting
    time_sort = timeit.timeit(lambda: bubble_list.sort(), number=1)
    print(f"Bubble Sort: {time_sort:.10f} seconds")

if __name__ == "__main__":
    test_bubble()