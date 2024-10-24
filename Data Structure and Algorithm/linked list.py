class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

#Add node at the end
def append(self, data):
    new_node = Node(data)
    if self.head is None:
        self.head = new_node
        return 
    last = self.head
    while last.next:
        last = last.next
        last.next = new_node

    #Display the linkedList
def display(self):
    current = self.head
    while current:
        print(current.data, end="->") 
        current = current.next
        print(None)      
