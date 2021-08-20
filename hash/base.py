class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    
    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key,value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def print(self):
        result = [] 
        for item in self.map:
            if item:
                result.append(item)
        print(result)

    def keys(self):
        arr = []
        for i in range(self.size):
            if self.map[i]:
                arr.append(self.map[i][0][0])
        print(arr)
    
    def values(self):
        arr = []
        for i in range(self.size):
            if self.map[i]:
                arr.append(self.map[i][0][1])
        print(arr)
    


hash = HashMap()
hash.add(8, 'value1')
hash.add(11, 'value2')
hash.add(12, 'value2')
hash.add('key3', 'value3')
hash.print()

