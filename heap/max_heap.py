class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = self.storage.index(value)
        self._bubble_up(index)

    def delete(self):
        deleted = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        self._sift_down(0)
        return deleted

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        # index = 0
        while index < len(self.storage):
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            if left_child < len(self.storage) - 1:
                if self.storage[left_child] > self.storage[index] and self.storage[right_child] < self.storage[index]:
                    self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
                    index += 1
                elif self.storage[right_child] > self.storage[index] and self.storage[left_child] < self.storage[index]:
                    self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
                    index += 1
                elif self.storage[index] < self.storage[left_child] and self.storage[index] < self.storage[right_child]:
                    if self.storage[left_child] > self.storage[right_child]:
                        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
                        index += 1
                    elif self.storage[right_child] > self.storage[left_child]:
                        self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
                        index += 1
            index += 1
