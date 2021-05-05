from node import Node


class LinkedList:

    def __init__(self):
        """
        Initializing variables
        head: points to the first node in the linked list
        """
        self.head = None

    def empty(self):
        """
        Returns True if linked list is empty and False otherwise
        """
        return self.head is None

    def add(self, value):
        """
        Adds the value to the linked list

        """
        if self.head is None:
            self.head = Node(value)
        else:
            rest = self.head
            self.head = Node(value)
            self.head.next = rest

    def delete(self, value):
        """
        Deletes the value from the linked list
        """
        return_head = self.head
        current = self.head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                return_head = self.head
                self.head = self.head.next
            else:
                return_head = previous.next
                previous.next = current.next

        return return_head