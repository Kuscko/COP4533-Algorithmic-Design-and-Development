import re

def check_html(file_path):
    # Reading the file content is O(n) where n is the number of characters in the file.

    # This is because reading the entire file content requires iterating over each character in the file once.
    with open(file_path, 'r') as f:
        content = f.read()
    
    stack = []
    
    # The re.findall() function is O(n) where n is the number of tags in the HTML content.

    # It scans the entire document to find all the tags and returns them as a list.
    tags = re.findall(r'<(\w+)|<\/(\w+)>', content)
    
    # The for loop is O(m) where m is the number of tags in the HTML content. 

    # Each tag is processed once in the loop and pushed or popped from the stack.
    for opening, closing in tags:
        if opening:
            stack.append(opening)
        elif closing:
            if not stack or stack.pop() != closing:
                return "Invalid HTML"
    
    # The final check is O(1) because it only checks if the stack is empty or not.
    return "Valid HTML" if not stack else "Invalid HTML"

# The overall time complexity of the check_html() function is O(n).
# This is because the overall most time consuming steps are reading the file content 
#      and finding all the tags in the HTML content.

file_path = input("Enter HTML file path: ")
result = check_html(file_path)
print(result)