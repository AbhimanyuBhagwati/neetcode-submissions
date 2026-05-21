class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        def return_cnt(x):
            _map = {}
            for i in x:
                if i in _map:
                    _map[i] += 1
                else:
                    _map[i] = 1
            return _map
        
        cnt_s = return_cnt(s)
        cnt_t = return_cnt(t)
        
        return cnt_s == cnt_t