class MergeStringList:
    def __init__(self):
        self.internal_list = []

    def add(self, string):
        self.internal_list.append(string)

    def sort(self):
        self.internal_list = self._merge_sort(self.internal_list)

    def _merge_sort(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = lst[:mid]
            right_half = lst[mid:]

            self._merge_sort(left_half)
            self._merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    lst[k] = left_half[i]
                    i += 1
                else:
                    lst[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                lst[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                lst[k] = right_half[j]
                j += 1
                k += 1

        return lst