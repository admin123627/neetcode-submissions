class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros_index = []
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zeros_index.append(i)
        output = []
        for i in range(len(nums)):
            if any(x != i for x in zeros_index):
                output.append(0)
            else:
                output.append(int(product / nums[i] if i not in zeros_index else product))
        return output
            


