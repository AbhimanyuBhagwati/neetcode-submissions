class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_copy = set(nums)
        cnt = 0

        for i in nums_copy:
            if (i - 1) in nums_copy:
                continue

            _cnt = 1
            _ele = i

            while _ele in nums_copy:
                if _ele + 1 not in nums_copy:
                    break
                _ele += 1
                _cnt += 1

            cnt = max(cnt, _cnt)

        return cnt