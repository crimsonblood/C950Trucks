# All the same?
class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item


class HashMap:
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

    # Create hash key
    def create_hash_key(self, key):
        return int(key) % len(self.map)

    # Insert key and value pair into hash table
    def insert(self, key, value):
        key_hash = self.create_hash_key(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Update key and value pair in hashtable
    def update(self, key, value):
        key_hash = self.create_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('There was an error with updating on key: ' + key)

    # Get a value from the hashtable
    def get_value(self, key):
        key_hash = self.create_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Delete a value from the hashtable
    def delete(self, key):
        key_hash = self.create_hash_key(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
