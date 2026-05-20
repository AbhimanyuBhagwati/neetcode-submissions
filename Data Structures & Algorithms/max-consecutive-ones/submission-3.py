class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        cnt= 0
        for i in nums:
            if i ==1:
                cnt +=1
                if max_cnt<cnt:
                    max_cnt = cnt
            else:
                cnt = 0

        return max_cnt
                
                