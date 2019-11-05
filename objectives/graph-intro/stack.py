class Stack:
    def __init__(self):
        self._storage = {}
        self._length = 0

    def __str__(self):
        return f"{self._storage}"

    def push(self, data):
        self._storage[self._length] = data
        self._length += 1

        return self._length

    def pop(self):
        if self._length:
            removed_item = self._storage[self._length - 1]
            del self._storage[self._length - 1]
            self._length -= 1

            return removed_item

    def length(self):
        return self._length


if __name__ == '__main__':
    myStack = Stack()
    myStack.push(10)
    myStack.push(20)
    myStack.push(30)

    myStack.pop()
    myStack.pop()
    myStack.pop()

    print(myStack)
