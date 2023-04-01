class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.prime = 10000001
        
    def _hash_func(self, key):
        hashed = 0
        for ch in key:
            hashed = (hashed * 263 + ord(ch)) % self.prime
        return hashed % self.size
        
    def add(self, key, value):
        hashed = self._hash_func(str(key))
        for i, (k, v) in enumerate(self.table[hashed]):
            if k == key:
                self.table[hashed][i] = (key, value)
                return
        self.table[hashed].append((key, value))
        
    def remove(self, key):
        hashed = self._hash_func(str(key))
        for i, (k, v) in enumerate(self.table[hashed]):
            if k == key:
                del self.table[hashed][i]
                return
        
    def find(self, key):
        hashed = self._hash_func(str(key))
        for k, v in self.table[hashed]:
            if k == key:
                return v
        return None


def read_queries():
    n = int(input())
    return [Query(str(input()).split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(str(r) if r is not None else "not found" for r in result))

def process_queries(queries):
    result = []
    contacts = HashTable(100000)
    for query in queries:
        if query.type == 'add':
            contacts.add(query.number, query.name)
        elif query.type == 'del':
            contacts.remove(query.number)
        else:
            result.append(contacts.find(query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
