class Node:

    def __init__(self, item, next=None):
        """
        Initializing variables

        item: stores a value
        next: points to the next node
        """
        self.item = item
        self.next = next

    def __str__(self):
        """
        String representation shows value stored
        """
        return str(self.item)
