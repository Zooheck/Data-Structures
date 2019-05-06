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
            self.tail.set_next(new_person)
            self.tail = new_person

    def dequeue(self):
        # there are no people in the queue
        if not self.head and not self.tail:
            print('The list is currently empty.')
            return None
        # if there is only one item in the list
        elif self.head == self.tail:
            person = self.head
            self.head = None
            self.tail = None
            print(f'{person.get_name()} has left the queue. The queue is now empty.')
            return person.get_name()

        else:
            person = self.head
            self.head = person.get_next()
            return person.get_name()

    def len(self):
        pass
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return int(count)
