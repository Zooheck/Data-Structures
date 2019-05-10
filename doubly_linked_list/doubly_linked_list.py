"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_value = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_value
            self.tail = new_value
            self.length += 1
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1

    def remove_from_head(self):
        # self.head.delete()
        # self.length -= 1
        if self.head == self.tail:
            deleted = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return deleted.value
        else:
            deleted = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return deleted.value

    def add_to_tail(self, value):
        node_value = ListNode(value)
        if not self.head and not self.tail:
            self.head = node_value
            self.tail = node_value
            self.length += 1
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.tail.next = None
            self.length += 1

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            # self.head.delete()
            deleted = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return deleted.value
        else:
            deleted = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return deleted.value

    def move_to_front(self, node):
        # node = ListNode(node)
        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):
        # node = ListNode(node)
        self.add_to_tail(node.value)
        self.delete(node)

    def delete(self, node):
        if node == self.head or self.head == self.tail:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    def get_max(self):
        max = self.head.value
        index = self.head
        while index.next != None:
            index = index.next
            if index.value > max:
                max = index.value
        return max
