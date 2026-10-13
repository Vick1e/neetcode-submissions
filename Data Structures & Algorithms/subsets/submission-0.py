class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]

        for num in nums:

            size = len(result)

            for i in range(size):
                newset = result[i]+[num]

                result.append(newset)

        return result