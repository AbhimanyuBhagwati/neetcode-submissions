class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_copy = set(nums)
        cnt = 0
        for ele in nums_copy:
            if (ele -1) not in nums_copy:
                _cnt = 1
                _ele = ele
                while (_ele +1) in nums_copy:
                    _cnt +=1
                    _ele+=1
                cnt = max(cnt, _cnt)
        return cnt