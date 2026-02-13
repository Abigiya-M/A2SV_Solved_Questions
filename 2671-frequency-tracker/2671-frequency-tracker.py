class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.freq_count = defaultdict(int)
        

    def add(self, number: int) -> None:
        curr = self.count[number]
        self.count[number] += 1

        if curr > 0:
            self.freq_count[curr] -= 1
            if self.freq_count[curr] == 0:
                del self.freq_count[curr]

        self.freq_count[self.count[number]] += 1

        

    def deleteOne(self, number: int) -> None:
        if number in self.count:
            cnt = self.count[number]

            self.count[number] -= 1
            self.freq_count[cnt] -= 1

            if self.count[number] == 0:
                del self.count[number]
            else:
                self.freq_count[self.count[number]] += 1
            
            if self.freq_count[cnt] == 0:
                del self.freq_count[cnt]
            
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] >  0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)