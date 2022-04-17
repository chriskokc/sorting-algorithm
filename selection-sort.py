# Selection Sort

class Array:
    def __init__(self, n):
        self.size = n
        self.arr = [None for i in range(n)]
        self.items = 0

    def insert(self, num):
        self.arr[self.items] = num
        self.items += 1

    def swap(self, i1, i2):
        temporary = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = temporary

    def selection_sort(self, length):
        # e.g [26, 15, 9, 59, 37, 1, 68, 32, 34]
        # for each element in the array (except the last element as it does not need to be sorted)
        for i in range(length - 1):
            min_value_index = i
            # find the smallest element
            for j in range(i + 1, length):
                if self.arr[j] < self.arr[min_value_index]:
                    min_value_index = j
            # swap the value
            self.swap(i, min_value_index)

