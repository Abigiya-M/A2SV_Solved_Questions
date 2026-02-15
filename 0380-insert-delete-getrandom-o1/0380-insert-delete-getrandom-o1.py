class RandomizedSet:

    def __init__(self):
        self.store_mp = defaultdict(int)
        self.store = []

    def insert(self, val: int) -> bool:
        if val in self.store_mp:
            return False
            
        self.store_mp[val] = len(self.store)
        self.store.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store_mp:
            return False
        ind = self.store_mp[val]
        last_num = self.store[-1]

        self.store[-1], self.store[ind] = self.store[ind], self.store[-1]

        self.store_mp[last_num] = ind

        self.store.pop()
        del self.store_mp[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.store)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()