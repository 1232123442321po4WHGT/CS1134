import random
from UnsortedArrayMap import UnsortedArrayMap

class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(UnsortedArrayMap.Item) and isinstance(curr_bucket):
            self.table[i] = None
        if isinstance(UnsortedArrayMap) and isinstance(curr_bucket):
            del curr_bucket[key]
        
        self.n -= 1
        if self.n < self.N // 4:
            self.rehash(self.N // 2)

    def __iter__(self):
        for curr_bucket in self.table:
            if curr_bucket == None:
                yield None
            else:
                for key in curr_bucket:
                    yield key

    def __contains__(self, key):
        try:
            val = self[key]
            if val != None:
                return True
            else:
                return False
        except KeyError:
            return False

    def rehash(self, new_size):
        oldlist = []
        for key in self:
            if key != None:
                value = self[key]
        self.__init__(new_size)
        for (key, val) in oldlist:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()