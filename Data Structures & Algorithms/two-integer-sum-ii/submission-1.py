class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        min, max = 0, len(numbers)-1
        while min < max:
            result = numbers[min] + numbers[max]
            if result > target:
                max -=1
            if result < target:
                min +=1
            if result == target:
                return [min+1, max+1]