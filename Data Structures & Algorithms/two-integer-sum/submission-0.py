class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _map = { }

        for ind, val in enumerate(nums):
            rem = target - val
            if rem in _map:
                return [_map[rem], ind]
            else:
                _map[val] = ind
        return []