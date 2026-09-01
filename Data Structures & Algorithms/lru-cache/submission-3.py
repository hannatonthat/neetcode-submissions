class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

        self.cache = defaultdict(int)

        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = value
        self.insert(key)
        if len(self.cache) > self.cap:
            val = self.head.next.val
            del self.cache[val]
            temp = self.head.next
            self.head.next = self.head.next.next
            temp.prev, temp.next = None, None
        
    def remove(self, key):
        if len(self.cache) == 1:
            temp = self.head.next
            self.head.next, self.tail.prev = self.tail, self.head
            return
        curr = self.head
        while curr.next.next and curr.next.val != key:
            curr = curr.next
        temp = curr.next
        curr.next = curr.next.next
        curr.next.prev = curr

    def insert(self, key):
        temp = self.tail.prev
        newNode = Node(key)
        newNode.next, newNode.prev = self.tail, temp
        temp.next, self.tail.prev = newNode, newNode