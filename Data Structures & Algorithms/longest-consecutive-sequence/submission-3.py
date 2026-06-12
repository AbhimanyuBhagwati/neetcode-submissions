class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums_set:
            if n - 1 in nums_set:
                continue

            count = 1
            cur = n

            while cur + 1 in nums_set:
                cur += 1
                count += 1

            longest = max(longest, count)

        return longest