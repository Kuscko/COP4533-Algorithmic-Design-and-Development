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

file_path = input("Enter HTML file path: ")
result = check_html_tags(file_path)
print(result)