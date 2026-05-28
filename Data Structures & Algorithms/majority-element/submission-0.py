class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = len(nums)/2
        map = {}
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i] +=1
        
        for k,v in map.items():
            if v >=maj_ele:
                return k