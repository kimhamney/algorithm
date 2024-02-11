class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqNum = 0
        for idx in nums:
            uniqNum ^= idx
        return uniqNum