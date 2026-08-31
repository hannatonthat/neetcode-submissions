class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = Node(key, value)
        self.insert(self.hash_map[key])

        if len(self.hash_map) > self.cap:
            temp = self.left.next
            self.remove(temp)
            del self.hash_map[temp.key]