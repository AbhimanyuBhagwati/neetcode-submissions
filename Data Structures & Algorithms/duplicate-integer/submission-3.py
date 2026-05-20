class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _dup = {}
        for i in range(len(nums)):
            if _dup.get(nums[i]) is not None:
                return True
            else:
                _dup[nums[i]] = i
        return False
