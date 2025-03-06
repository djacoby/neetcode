"""
Design Hashmap

Leetcode 706 - https://leetcode.com/problems/design-hashmap/

Explanation:

"""

class MyHashMap:

    def __init__(self, size = 100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: int):
        prime = 31
        return (key * prime) % self.size

    def put(self, key: int, value):
        """Insert or update a key-value pair."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        # Check if key already exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update value
                return

        # If key not found, append new pair
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """Retrieve the value associated with a key."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for k, v in bucket:
            if k == key:
                return v  # Return the value if found
        return -1  # Return -1 if key not found

    def remove(self, key: int) -> None:
        """Remove a key-value pair from the HashMap."""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return
            
    def __str__(self):
        """String representation of the HashMap."""
        elements = []
        for bucket in self.table:
            elements.extend([f"{k}: {v}" for k, v in bucket])
        return "{" + ", ".join(elements) + "}"

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

myHashMap = MyHashMap();
myHashMap.put(1, 1); # The map is now [[1,1]]
myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
print(myHashMap.__str__())
myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]