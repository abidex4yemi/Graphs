class Queue:
    def __init__(self):
        self._storage = {}
        self._length = 0
        self._startIndex = 0

    def __str__(self):
        return f"{self._storage}"

    def enqueue(self, data):
        if data is not None:
            self._storage[self._length + self._startIndex] = data

            self._length += 1

    def dequeue(self):
        if self._length > 0:
            removed_item = self._storage[self._startIndex]
            del self._storage[self._startIndex]

            self._length -= 1
            self._startIndex += 1

            return removed_item

    def length(self):
        return self._length


if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue(10)
    myQueue.enqueue(5)
    myQueue.enqueue(2)

    myQueue.dequeue()

    myQueue.enqueue(1)

    print(myQueue)
