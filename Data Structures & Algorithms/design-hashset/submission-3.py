class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.arr = [None for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        self.__addInternal(key)
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
                self.__addInternal(node.val, False)
                node = node.next

    def __addInternal(self, key, checkExistence = True):
        position = key % self.capacity
        if checkExistence and self.contains(key):
            return

        newNode = LinkedNode(key)
        newNode.next = self.arr[position]
        self.arr[position] = newNode
        self.size += 1
            
    def remove(self, key: int) -> None:
        position = key % self.capacity
        previous = None
        node = self.arr[position]
        while node is not None:
            if node.val != key:
                previous = node
                node = node.next
                continue 
            if previous is not None:
                previous.next = node.next
            else:
                self.arr[position] = node.next
            self.size -= 1
            return           
        

    def contains(self, key: int) -> bool:
        position = key % self.capacity
        node = self.arr[position]
        while node is not None:
            if node.val == key:
                return True
            node = node.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)