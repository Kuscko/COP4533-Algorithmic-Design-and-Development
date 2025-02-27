class BubbleStringList:
    def __init__(self):
        self.internal_list = []

    def add(self, string):
        self.internal_list.append(string)

    def sort(self):
        n = len(self.internal_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.internal_list[j] > self.internal_list[j+1]:
                    self.internal_list[j], self.internal_list[j+1] = self.internal_list[j+1], self.internal_list[j]