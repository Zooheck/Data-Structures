class Person:
    def __init__(self, name, next_person=None):
        self.name = name
        self.next_person = next_person

    def get_name(self):
        return self.name

    def get_next(self):
        return self.next_person

    def set_next(self, new_next_person):
        self.next_person = new_next_person


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
        self.head = None
        self.tail = None

    def enqueue(self, person):
        new_person = Person(person)
        # If the queue is currently empty...
        if not self.head and not self.tail:
            # then our new_person both starts and ends the queue, since he is the only person currently in line
            self.head = new_person
            self.tail = new_person
        # If the queue has more than one...
        else:
          # the
            self.tail.set_next(new_person)
            self.tail = new_person

    def dequeue(self):
        pass

    def len(self):
        pass
