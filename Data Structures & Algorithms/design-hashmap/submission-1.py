class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.arr = [None for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        self.__putInternal(key, value)
        self.__resizeIfNeeded()
        

    def __resizeIfNeeded(self):
        if self.size / self.capacity < .7:
            return
        oldArr = self.arr
        self.capacity *= 2
        self.size = 0
        self.arr = [None for _ in range(self.capacity)]
        for i in range(len(oldArr)):
            node = oldArr[i]
            while node is not None:
                self.__putInternal(node.key, node.value, False)
                node = node.next

    def __putInternal(self, key, value, checkExistence=True):
        position = key % self.capacity
        if checkExistence:
            node = self.arr[position]
            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next

        newNode = LinkedNode(key, value)
        newNode.next = self.arr[position]
        self.arr[position] = newNode
        self.size += 1

    def get(self, key: int) -> int:
        position = key % self.capacity
        node = self.arr[position]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        position = key % self.capacity
        previous = None
        node = self.arr[position]
        while node is not None:
            if node.key != key:
                previous = node
                node = node.next
                continue 
            if previous is not None:
                previous.next = node.next
            else:
                self.arr[position] = node.next
            self.size -= 1
            return    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)