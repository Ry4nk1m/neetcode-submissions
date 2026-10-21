class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        l = 0
        r = l
        curr = 0
        while r < len(s):
            if s[r] in seen:
                curr = 0
                l += 1
                r=l
                seen.clear()
            else:
                seen.add(s[r])
                curr += 1
                longest = max(longest, curr)
                r += 1
        return longest