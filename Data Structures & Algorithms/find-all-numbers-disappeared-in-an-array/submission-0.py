class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        _not_pre =[]


        for i in range(1, len(nums)+1):
            if i in nums:
                continue
            else:
                _not_pre.append(i)
        return _not_pre

