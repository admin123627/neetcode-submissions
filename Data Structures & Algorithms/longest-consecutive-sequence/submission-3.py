class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maximum = 0
        starts = set()
        for i in nums:
            if i - 1 not in nums_set:
                starts.add(i)
        for i in starts:
            count = 1
            curr = i
            while (curr + 1) in nums_set:
                count += 1
                curr += 1
            maximum = max(maximum, count)
        return maximum


        