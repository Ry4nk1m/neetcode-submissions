class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = defaultdict(int)
        res, l, freq = 0, 0, 0
        for r in range(len(s)):
            charMap[s[r]] += 1
            freq = max(freq, charMap[s[r]])
            while (r - l + 1) - freq > k:
                charMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res