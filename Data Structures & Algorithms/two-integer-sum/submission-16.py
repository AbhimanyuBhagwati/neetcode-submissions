class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = {}
        for ind, val in enumerate(nums):
            _rem= target - val
            if _rem in _map:
                return [_map[_rem], ind]
            else:
                _map[val] = ind
        return []