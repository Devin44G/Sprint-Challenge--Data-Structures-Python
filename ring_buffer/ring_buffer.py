class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    class __Full:
        def append(self, x):
            self.data[self.curr] = x
            self.curr = (self.curr + 1) % self.capacity

        def get(self):
            return self.data

    def append(self, item):
        self.data.append(item)
        if len(self.data) == self.capacity:
            self.curr = 0
            self.__class__ = self.__Full

    def get(self):
        return self.data
