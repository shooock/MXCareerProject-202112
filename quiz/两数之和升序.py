class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return numbers
        left = 0
        len_list= len(numbers)
        right = len_list -1
        while left < right:
            sum_num = numbers[left] + numbers[right]
            if sum_num == target:
                return [left+1, right+1]
            elif sum_num != target:
                if sum_num < target:left += 1
                else:right -= 1