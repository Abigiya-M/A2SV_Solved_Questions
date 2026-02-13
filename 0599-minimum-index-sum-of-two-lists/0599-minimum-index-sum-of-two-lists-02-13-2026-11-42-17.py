class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        min_sum = 100

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    s = i + j

                    if s < min_sum:
                        min_sum = s
                        result = [list1[i]]

                    elif s == min_sum:
                        result.append(list1[i])

        return result
