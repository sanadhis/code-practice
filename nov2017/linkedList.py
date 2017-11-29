class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node and current_node.next:
                current_node  = current_node.next
            current_node.next = node

    def delete(self, data):
        current_node = self.head
        while current_node and current_node.next:
            previous_node = current_node
            current_node  = current_node.next
            if current_node.data == data:
                previous_node.next = current_node.next
                break
    
    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            nextNode          = current_node.next
            current_node.next = previous_node
            previous_node     = current_node
            current_node      = nextNode
        self.head = previous_node

    def __str__(self):
        string = ""
        p = self.head
        while p:
            string += p.data
            p = p.next
        return string

ll = LinkedList()
ll.add("A")
ll.add("5")
ll.add("c")
print(ll)

ll.reverse()
print(ll)

ll.reverse()
print(ll)

ll.delete("5")
print(ll)

ll.reverse()
print(ll)

ll.delete("4")
print(ll)