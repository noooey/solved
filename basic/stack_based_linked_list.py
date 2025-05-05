class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        cur = self.top
        while cur:
            count += 1

if __name__ == "__main__":
    stack = LinkedListStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.pop())
    print(stack.peek())
    print(stack.is_empty())
