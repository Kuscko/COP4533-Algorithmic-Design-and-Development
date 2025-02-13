import timeit

def check_html_tags(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    stack = []
    i = 0
    
    while i < len(content):
        if content[i:i+2] == '</':
            j = content.find('>', i)
            if j == -1 or stack.pop() != content[i+2:j]:
                return "Invalid HTML"
            i = j + 1
        elif content[i] == '<':
            j = content.find('>', i)
            if j == -1:
                return "Invalid HTML"
            stack.append(content[i+1:j])
            i = j + 1
        else:
            i += 1
    
    return "Valid HTML" if not stack else "Invalid HTML"

def benchmark():
    test_file = "C://Users/Patrick/Desktop/School/COP4533-Algorithmic-Design-and-Development/Assignment_2_Algorithms/index.html"  # Replace with the path to your test HTML file

    timings = []
    for _ in range(5):  # Run 5 times
        start_time = timeit.default_timer()
        vaild_check = check_html_tags(test_file)
        end_time = timeit.default_timer()
        timings.append(end_time - start_time)
    
    for i, timing in enumerate(timings, 1):
        print(f"Run {i}: {timing:.6f} seconds | Result: {vaild_check}")
    
    average_time = sum(timings) / len(timings)
    print(f"\nAverage Time: {average_time:.6f} seconds")

if __name__ == "__main__":
    benchmark()