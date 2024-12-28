class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_start(self, data):
        """Insert a new node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, node):
        """Delete the given node from the linked list."""
        temp = self.head

        # If the head node itself is the node to be deleted
        if temp == node:
            self.head = temp.next
            temp = None
            return

        # Search for the node to be deleted
        prev = None
        while temp and temp != node:
            prev = temp
            temp = temp.next

        # If the node was not present in the list
        if not temp:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def search(self, key):
        """Search for a node with the given key and return True if found, else False."""
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        """Display the entire linked list."""
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements


