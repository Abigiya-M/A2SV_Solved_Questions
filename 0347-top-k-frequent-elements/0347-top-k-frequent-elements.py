class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        cnt_freq = defaultdict(list)

        for key, value in cnt.items():
            cnt_freq[value].append(key)
        
        keys = sorted(cnt.values())

        ans = []
        for i in range(len(keys)-1, -1, -1):
            if len(ans) == k:
                return ans
            
            ans.append(cnt_freq[keys[i]].pop())
        
        return ans
