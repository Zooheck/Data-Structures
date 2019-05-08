class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        # if the base value is the target...
        if self.value == target:
            return True
        # if the target is less than the base value, examine the left side
        elif target < self.value:
            # if there's nothing left of the base, the target does not exist
            if not self.left:
                return False
            # return true if target is equal to left of base
            elif target == self.left.value:
                return True
            # if target is unequal to left of base, run the function again with the left value as the new base
            else:
                self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            elif target == self.right.value:
                return True
            else:
                self.right.contains(target)

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        pass
