def find_max(lst):
    if len(lst) == 0:
        raise ValueError("Empty list")
    if len(lst) == 1:
        return lst[0]
    else:
        # find the maximum of the rest of the list using a recursive call and max() function
        return max(lst[0], find_max(lst[1:]))

def main():
    test_cases = [
        [1, 2, 3, 4, 5],
        [-5, -2, -1, -3],
        [10, 5, 15, 20, 25],
        [42],
        []
    ]
    
    for case in test_cases:
        try:
            max_val = find_max(case)
            print(f"List: {case}, Maximum: {max_val}")
        except ValueError:
            print(f"List: {case}, Error: Empty list")

if __name__ == "__main__":
    main()