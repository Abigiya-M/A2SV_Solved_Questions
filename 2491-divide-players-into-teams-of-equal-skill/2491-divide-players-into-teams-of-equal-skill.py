class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        fir = -1
        skill.sort()
        left, right = 0, len(skill) - 1
        cnt = 0
        while left < right:
            prod = skill[left] * skill[right]
            curr = skill[left] + skill[right]
            if fir == -1:
                fir  = curr
            else:
                if curr != fir:
                    return -1
            cnt += prod
            left += 1
            right -= 1
        
        return cnt
                



