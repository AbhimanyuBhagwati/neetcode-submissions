class Solution:
    def isValid(self, s: str) -> bool:
        _mapp= {

        '(':')', '{':'}', '[':']', 
        }
        open_brc = ['[','{', '(']
        _track = []
        for i in s:
            if len(_track) == 0 and i not in open_brc: return False
            if i in open_brc:
                _track.append(i)
            else:
                if _mapp.get(_track[-1]) == i:
                    del _track[-1]
                else:
                    return False
        
        if len(_track) == 0:
            return True
        else:
            return False