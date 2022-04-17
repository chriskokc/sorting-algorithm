# heap sort

class Array:
    def __init__(self, n):
        self.size = n
        self.arr = [None for i in range(n)]
        self.items = 0

    def insert(self, num):
        self.arr[self.items] = num
        self.items += 1

    def swap(self, index_1, index_2):
        temp = self.arr[index_1]
        self.arr[index_1] = self.arr[index_2]
        self.arr[index_2] = temp

    def get_left_child(self, parent_index):
        left_child_index = parent_index * 2 + 1
        return left_child_index

    def get_parent(self, child_index):
        parent_index = (child_index - 1) // 2
        return parent_index

    def is_leaf(self, index):
        last_index = self.items - 1
        parent_index_of_last = self.get_parent(last_index)
        if (index > parent_index_of_last) and (index <= last_index):
            return True
        return False

    def fix_down(self, index):
        # while the current node is not a leaf node
        while not self.is_leaf(index):
            # compare with the greater of its child (i.e L or R)
            # check if its right child exists, by checking j is not the last element
            # then compare the left and right child
            left_child_index = self.get_left_child(index)
            right_child_index = left_child_index + 1
            j = left_child_index
            if j != self.items - 1 and self.arr[left_child_index] < self.arr[right_child_index]:
                j = right_child_index
            # if it is larger, exit the loop
            if self.arr[index] >= self.arr[j]:
                break
            # else
            self.swap(index, j)
            # update the current index after swapping with child
            index = j

    def heapify(self):
        # from the last node, get its parent
        last_index = self.items - 1
        parent_index = self.get_parent(last_index)
        # for all parent nodes, call fix down to preserve the heap's order property,
        # decrement the parent index by 1
        for i in range(parent_index, -1, -1):
            self.fix_down(i)

    def heap_sort(self):
        # turn our array into a max heap
        self.heapify()
        # store the value of current number of items
        no_of_items = self.items
        # repeat the following until the number of item is less than or equal to 1
        while self.items > 1:
            # swap with the last element
            self.swap(0, self.items - 1)
            # decrease the array size by 1
            self.items -= 1
            # fix down to preserve the heap's order property
            self.fix_down(0)
        # resume the original number of items after exiting the loop
        self.items = no_of_items
