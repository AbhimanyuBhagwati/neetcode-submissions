class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _is_1s= None
        cnt_1s = 0
        max_cnt = 0
        if len(nums) <=1:
            pass
        if nums[0] ==1:
            _is_1s = True
            cnt_1s +=1
            max_cnt = 1
        else:
            _is_1s = False

        for i in range(1, len(nums)):
            if nums[i] ==1:
                _is_1s =True
                cnt_1s +=1
                if max_cnt < cnt_1s :
                    max_cnt = cnt_1s
            else:
                cnt_1s = 0
                _is_1s = False
        return max_cnt