class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        index1 = 0
        index2 = len(heights) - 1
        while index1 < index2:
            area = (index2 - index1) * min(heights[index1], heights[index2])
            maximum = max(area, maximum)
            if heights[index1] < heights[index2]:
                index1 += 1
            else:
                index2 -= 1
        return maximum

            


        