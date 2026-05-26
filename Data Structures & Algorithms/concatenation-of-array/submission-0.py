class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        _new = []
        for j in range(2):
            for i in range(len(nums)):
                _new.append(nums[i])
        return _new