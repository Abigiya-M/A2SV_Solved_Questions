class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def calc(nums, k):
            N = len(nums)
            check = defaultdict(int)
            left = 0
            count = 0
            for right in range(N):
                check[nums[right]] += 1
                while len(check) > k:
                    check[nums[left]] -= 1
                    if check[nums[left]] == 0:
                        del check[nums[left]]
                    left += 1
    
    
                count += (right - left + 1)
    
            return count
        return calc(nums, k) - calc(nums, k-1)
