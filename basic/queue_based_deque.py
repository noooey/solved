from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    dq = DequeQueue()
    dq.enqueue(1)
    dq.enqueue(2)
    dq.enqueue(3)
    print(dq.dequeue())
    print(dq.front())
    print(dq.is_empty())
