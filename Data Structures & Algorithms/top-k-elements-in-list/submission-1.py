class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        c = counter.most_common(k)
        for i in range(len(c)):
            res.append(c[i][0])
        return res