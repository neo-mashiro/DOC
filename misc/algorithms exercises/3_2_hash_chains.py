# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.index = int(query[1])
        else:
            self.string = query[1]

class QueryProcessor:

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, m):
        self.arr = [[] for _ in range(m)]  # create the nested array for chaining
        self.m = m  # number of slots in the array self.arr, also the cardinality of _hash_func()

    def _hash_func(self, string):
        ''' polynomial hash function to hash a string into a key '''
        key = 0
        for char in reversed(string):
            key = (key * self._multiplier + ord(char)) % self._prime  # ord(char) returns the ASCII code
        return key % self.m

    def insert(self, string):
        key = self._hash_func(string)
        if string in self.arr[key]:
            return
        self.arr[key].append(string)

    def delete(self, string):
        key = self._hash_func(string)
        for index, e_str in enumerate(self.arr[key]):
            if string == e_str:
                self.arr[key].pop(index)
                break

    def find(self, string):
        key = self._hash_func(string)
        for e_str in self.arr[key]:
            if e_str == string:
                print("yes")
                return
        print("no")

    def check(self, key):
        if key < 0 or key >= self.m:
            print()
        strings_in_slot = self.arr[key][::-1]
        print(' '.join(strings_in_slot))

    def process_query(self, query):
        if query.type == "check":
            self.check(query.index)
        elif query.type == "add":
            self.insert(query.string)
        elif query.type == "del":
            self.delete(query.string)
        else:
            self.find(query.string)


if __name__ == '__main__':
    ''' note that the number of buckets m is given for this problem, so m is fixed,
        so we must build a static fixed-sized hash table that does not rehash().
    '''
    m = int(input())  # number of slots/buckets
    n = int(input())  # number of queries
    proc = QueryProcessor(m)

    for i in range(n):
        query = Query(input().split())
        proc.process_query(query)
