class QuickStringList:
    def __init__(self):
        self.internal_list = []

    def add(self, string):
        self.internal_list.append(string)

    def sort(self):
        self._quick_sort(0, len(self.internal_list) - 1)

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.internal_list[high]
        i = low - 1
        for j in range(low, high):
            if self.internal_list[j] < pivot:
                i += 1
                self.internal_list[i], self.internal_list[j] = self.internal_list[j], self.internal_list[i]
        self.internal_list[i + 1], self.internal_list[high] = self.internal_list[high], self.internal_list[i + 1]
        return i + 1