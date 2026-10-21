class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l = 0
        r = len(heights)-1
        width = len(heights)-1
        while l < r:
            result = max(result, (width*min(heights[l], heights[r])))
            if heights[l]<heights[r]:
                l += 1
            elif heights[r]<heights[l]:
                r -= 1
            else:
                l += 1
            width -= 1
        return result