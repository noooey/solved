class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # Pointer pointing to the next node.

class LinkedList:
    def __init__(self):
        self.head = None   # Head pointer pointing to the first node.

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                return
            cur = cur.next
        new_node.next = cur.next

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and cur.next.data != data:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.display()
    ll.append(2)
    ll.display()
    ll.append(3)
    ll.display()
    ll.insert(1, 10)
    ll.display()
