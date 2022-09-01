class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, l = 0, 0
        myset = set()
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            myset.add(s[r])
            ans = max(ans, r - l + 1)
        return ans
