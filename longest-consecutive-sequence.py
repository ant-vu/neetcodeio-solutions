class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        ans = 0
        for i in nums:
            if i - 1 not in myset:
                length = 1
                while i + length in myset:
                    length += 1
                ans = max(ans, length)
        return ans
