class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in seen:
                res = max(res, i-l+1)
            else:
                if seen[s[i]] < l:
                    res = max(res, i-l+1)
                else:
                    l = seen[s[i]] + 1
            seen[s[i]] = i
        return res
