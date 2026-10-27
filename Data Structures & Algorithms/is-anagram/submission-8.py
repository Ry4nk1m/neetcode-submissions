class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortedS = defaultdict(int)
        sortedT = defaultdict(int)
        for i in range(len(s)):
            sortedS[s[i]] += 1
            sortedT[t[i]] += 1
        return sortedS == sortedT