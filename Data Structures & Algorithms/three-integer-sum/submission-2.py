class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        solution = []
        for i in range(len(sorted_nums) - 2):
            target = -sorted_nums[i]
            index1 = i + 1
            index2 = len(sorted_nums) - 1
            num = sorted_nums[index1] + sorted_nums[index2]
            
            while index1 < index2:
                if num < target:
                    index1 += 1
                elif num == target:
                    found = [sorted_nums[i], sorted_nums[index1], sorted_nums[index2]]
                    if found not in solution:
                        solution.append(found)
                    index2 -= 1
                else:
                    index2 -= 1 
                num = sorted_nums[index1] + sorted_nums[index2]

                
        return solution
                
                

        