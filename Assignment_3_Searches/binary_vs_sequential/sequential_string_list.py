class SequentialStringList:
    def __init__(self):
        self.internal_list = []

    def add(self, string):
        self.internal_list.append(string)

    def find(self, string):
        for item in self.internal_list:
            if item == string:
                return item
        return None