'''
Chase M. Peak
-stack abstract data structure
-array-based implementation
'''

class Stack():

    def __init__(self, capacity):
        if type(capacity) != int:
            raise ValueError('invalid capacity input')
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0


    def is_empty(self):
        return self.num_items == 0


    def is_full(self):
        return self.num_items == self.capacity


    def push(self, item):
        if self.is_full():
            raise IndexError('stack is full')
        self.items[self.num_items] = item
        self.num_items += 1


    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        self.num_items -= 1
        return self.items[self.num_items]


    def size(self):
        return self.capacity


    def peek(self):
        return self.items[self.num_items - 1]


    def resize(self, capacity):
        if self.num_items > capacity:
            raise IndexError('invalid capacity input')
        elif type(capacity) != int:
            raise ValueError('invalid capacity input')
        self.items += [None] * abs(self.capacity - capacity)
        self.capacity = capacity
