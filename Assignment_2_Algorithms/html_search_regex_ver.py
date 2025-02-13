import re
import timeit

def check_html(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    stack = []

    tags = re.findall(r'<(\w+)|<\/(\w+)>', content)

    for opening, closing in tags:
        if opening:
            stack.append(opening)
        elif closing:
            if not stack or stack.pop() != closing:
                return "Invalid HTML"
    
    return "Valid HTML" if not stack else "Invalid HTML"


def benchmark():
    test_file = "C://Users/<Username>/Path/To/index.html"  # Replace with the path to your test HTML file

    timings = []
    for _ in range(5):  # Run 5 times
        start_time = timeit.default_timer()
        vaild_check = check_html(test_file)
        end_time = timeit.default_timer()
        timings.append(end_time - start_time)
    
    for i, timing in enumerate(timings, 1):
        print(f"Run {i}: {timing:.6f} seconds | Result: {vaild_check}")
    
    average_time = sum(timings) / len(timings)
    print(f"\nAverage Time: {average_time:.6f} seconds")

if __name__ == "__main__":
    benchmark()