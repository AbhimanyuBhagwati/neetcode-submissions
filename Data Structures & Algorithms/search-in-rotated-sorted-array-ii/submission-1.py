class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        _nums_copy = deepcopy(set(nums))
        if target in _nums_copy:
            return True
        else:
            return False