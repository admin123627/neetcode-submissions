class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = [1, len(numbers)]
        num = numbers[solution[0] - 1] + numbers[solution[1] - 1]
        while num != target:
            if num < target:
                solution[0] += 1
            else:
                solution[1] -= 1
            num = numbers[solution[0] - 1] + numbers[solution[1] - 1]
        return solution

        