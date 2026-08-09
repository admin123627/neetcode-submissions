class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        for i in nums:
            if i not in nums_map:
                nums_map[i] = 1
            else:
                nums_map[i] += 1
        nums_list = nums_map.items()
        sorted_nums_list = []
        for i in nums_list:
            sorted_nums_list.append(i[::-1])
        sorted_nums_list = sorted(sorted_nums_list)
        to_return = []
        for i in range(min(k, len(sorted_nums_list))):
            to_return.append(sorted_nums_list[len(sorted_nums_list) - 1 - i][1])
        return to_return
        