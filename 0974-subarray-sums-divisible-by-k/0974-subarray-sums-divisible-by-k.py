class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)
        store[0] = 1

        running = 0
        ans = 0

        for i, n in enumerate(nums):
            running = (running + n) % k

            if running in store:
                ans += store[running]
            store[running] += 1
        
        return ans