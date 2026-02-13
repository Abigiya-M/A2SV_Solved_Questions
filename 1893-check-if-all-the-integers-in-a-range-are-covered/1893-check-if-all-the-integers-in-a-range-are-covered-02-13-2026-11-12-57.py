class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            covered = False

            for i in range(len(ranges)):
                if ranges[i][0] <= num and ranges[i][1] >= num:
                    covered = True
                    break

            if not covered:
                return False

        return True
