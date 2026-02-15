class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for val in nums:
            if val % 2:
                continue
            even_sum += val
        
        answer = []
        for val, ind in queries:
            updated = nums[ind] + val

            if updated % 2 == 0:
                if nums[ind] % 2 == 0:
                    even_sum += val
                else:
                    even_sum += updated
            else:
                if nums[ind] % 2 == 0:
                    even_sum -= nums[ind]
            
            answer.append(even_sum)
            nums[ind] = updated

        
        return answer

