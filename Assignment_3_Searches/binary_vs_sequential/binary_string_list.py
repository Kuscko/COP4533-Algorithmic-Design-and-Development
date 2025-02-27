class BinaryStringList:
    def __init__(self):
        self.internal_list = []

    def add(self, string):
        self.internal_list.append(string)
        self.internal_list.sort()  # Ensures the list is sorted for binary search

    def find(self, string):
        left, right = 0, len(self.internal_list) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.internal_list[mid] == string:
                return string
            elif self.internal_list[mid] < string:
                left = mid + 1
            else:
                right = mid - 1
        return None