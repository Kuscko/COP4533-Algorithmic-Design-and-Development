class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list
class LinkedList:
    # __init__() method to initialize the linked list
    def __init__(self):
        self.head = None
        self.tail = None
 
    # __str__() method to return a string representation of the linked list
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    # __setitem__() method to set the value of an element at a specific index in the linked list    
    def __setitem__(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("list index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = value
    
    # __delitem__() method to delete an element at a specific index in the linked list
    def __delitem__(self, index):
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next

    # __iter__() method to iterate through the linked list
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    # __contains__() method to check if an element is present in the linked list
    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False
    
    # __len__() method to get the length of the linked list
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # __getitem__() method to get the element at a specific index in the linked list
    def __getitem__(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # pop() method to remove the last element from the linked list
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            if prev:
                prev.next = None
            self.tail = prev

    # pop_at_index() method to remove the element at a specific index from the linked list
    def pop_at_index(self, index):
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next

    # insert() method to insert an element at a specific index in the linked list
    def insert(self, index, data):
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # reverse() method to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # extend() method to extend the linked list with another linked list
    def extend(self, other):
        self.tail.next = other.head
        self.tail = other.tail

    # clear() method to clear the linked list
    def clear(self):
        self.head = None
        self.tail = None
        self.data = None
        self.next = None