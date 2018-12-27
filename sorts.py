class Sorts:
    def __init__(self):
        self.list = None


    def selection_sort(self):
        for i in range(len(self.list)):
            min_index = i
            for j in range(i + 1, len(self.list)):
                if self.list[j] < self.list[min_index]:
                    min_index = j
            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]


    def insertion_sort(self):
        for i in range(len(self.list) - 1):
            j = i + 1
            while j > 0:
                if self.list[j] < self.list[j - 1]:
                    self.list[j], self.list[j - 1] = self.list[j - 1], self.list[j]
                elif list[j] >= list[j - 1]:
                    j = 0
                j -= 1
