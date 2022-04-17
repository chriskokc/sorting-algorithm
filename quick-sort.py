# Quick Sort
# divide and conquer


class Array:
    def __init__(self, n):
        self.arr = [None for i in range(n)]
        self.size = n
        self.items = 0

    def insert(self, num):
        self.arr[self.items] = num
        self.items += 1

    def swap(self, i1, i2):
        temporary = self.arr[i1]
        self.arr[i1] = self.arr[i2]
        self.arr[i2] = temporary

    def quick_sort_range(self, first_index, last_index):
        # get a pivot
        pivot = self.arr[first_index]
        # do partition
        # handle base case of recursion, i.e only 1 or 0 element in a group
        # if there is only 1 or 0 element, finish the whole function
        if last_index <= first_index:
            return
        pos = last_index
        # start from the last element of the sub-array (i.e excluding the first element pivot)
        for i in range(last_index, first_index, -1):
            # if the value is greater than pivot
            if self.arr[i] > pivot:
                # swap value with pos value (i.e put larger value at the back)
                self.swap(i, pos)
                # decrement pos
                pos -= 1
        # at the end of an iteration, put the pivot between the subgroups
        self.swap(first_index, pos)
        # repeat with recursion with the left and right subgroups
        self.quick_sort_range(pos + 1, last_index)
        self.quick_sort_range(first_index, pos - 1)

    def quick_sort(self):
        first_index = 0
        last_index = self.items - 1
        self.quick_sort_range(first_index, last_index)

