"""
Design Hashset

Leetcode 705 - https://leetcode.com/problems/design-hashset/

Explanation:
- Constructor sets the size (default 100), and instantiates a 2d array of buckets of set size
- Private hashing function creates a hash by multiplying the key by 31 (prime number) then returning the remainder after dividing by the size


"""

class MyHashSet:

    def __init__(self, size = 100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: int):
        prime = 31
        return (key * prime) % self.size

    def add(self, key: int) -> None:
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        if key not in bucket: 
            bucket.append(key)

    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        bucket = self.table[hash_index]
        
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        return key in bucket

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
