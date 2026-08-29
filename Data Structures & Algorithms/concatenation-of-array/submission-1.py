class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0]*(2*n)
        for i, num in enumerate(nums):
            count[i] = count[i+n] = num
        return count