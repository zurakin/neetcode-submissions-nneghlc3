class Node:
    def __init__(self, key: int, val: int, previous = None, next = None):
        self.key = key
        self.val = val
        self.previous = previous
        self.next = next
    

# lru - ... - mru

class LRUCache:

    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.capacity = 0
        self.lruNode = Node(-1, -1, None, None)
        self.mruNode = Node(-1, -1, self.lruNode, None)
        self.lruNode.previous = self.mruNode
        self.dict = {}
        

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]

        # remove node from linked list
        node.previous.next = node.next
        node.next.previous = node.previous

        # making the node the new mru Node
        # 1- attaching node to previous lru
        node.previous= self.mruNode.previous
        self.mruNode.previous.next = node

        # 2- attaching node to mruNode
        node.next = self.mruNode
        self.mruNode.previous = node
        print("get: ", key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].val = value
            self.get(key)
            return

        if self.capacity >= self.maxCapacity:
            nodeToRemove = self.lruNode.next
            nodeToRemove.previous.next = nodeToRemove.next
            nodeToRemove.next.previous = nodeToRemove.previous
            del self.dict[nodeToRemove.key]
            self.capacity -= 1

        newNode = Node(key, value, self.mruNode.previous, self.mruNode)
        self.mruNode.previous.next = newNode
        self.mruNode.previous = newNode
        self.dict[key] = newNode
        self.capacity += 1
        
