import random
from UnsortedArrayMap import UnsortedArrayMap

class Node:
    
    def __init__(self, val, prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

    def __hash__(self):
        return hash(self.val)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and  self.val == other.val

class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    class Node:
        def __init__(self, val, prev = None, nxt = None):
            self.val = val
            self.prev = prev
            self.nxt = nxt

        def __hash__(self):
            return hash(self.val)

        def __eq__(self, other):
            return isinstance(other, self.__class__) and  self.val == other.val
        
    def __init__(self, N=64):
        self.N = N
        self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)
        self.head = Node(None)
        self.tail = self.head

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        key = Node(key)
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        key = Node(key)
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)

        if (new_size > old_size):
            self.n += 1
            self.tail.nxt = key
            key.prev = self.tail
            self.tail = self.tail.nxt
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        key = Node(key)
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        target_key = None
        for bucket_key in curr_bucket:
            if bucket_key == key:
                target_key = bucket_key
                break
        del curr_bucket[key]
        self.n -= 1
        target_key.prev.nxt = target_key.nxt

        if target_key.nxt == None:
            self.tail = target_key.prev
        else:
            target_key.nxt.prev = target_key.prev
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):

         curr = self.head.nxt
         while curr != None:
             yield curr.val
             curr = curr.nxt

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key.val, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()
