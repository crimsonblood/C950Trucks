class HashMap:
    # HashMap init constructor, initializes to a capacity of 10 for all package info
    # Space-time complexity -> O(1)
    def __init__(self, capacity=10):
        self.map = []
        for _ in range(capacity):
            self.map.append([])

    # Create hash key
    # Space-time complexity -> O(1)
    def create_key(self, key):
        return int(key) % len(self.map)

    # Get a value from the hashtable
    # Space-time complexity -> O(N)
    def get_value(self, key):
        key_hash = self.create_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes a value from the hashtable
    # Space-time complexity -> O(N)
    def delete(self, key):
        key_hash = self.create_key(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    # Inserts key and value pair into hash table
    # Space-time complexity -> O(N)
    def insert(self, key, value):
        key_hash = self.create_key(key)
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

    # Updates key and value pair in hashtable
    # Space-time complexity -> O(N)
    def update(self, key, value):
        key_hash = self.create_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error updating key: ' + key)
