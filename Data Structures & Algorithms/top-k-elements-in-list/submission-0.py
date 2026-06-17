class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre_cnt = {}
        for i in nums:
            if i not in fre_cnt:
                fre_cnt[i] = 0
            fre_cnt[i] +=1
        sorted_items = sorted(fre_cnt.items(), key=lambda x: x[1], reverse=True)

        return [num for num, count in sorted_items[:k]]