class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        _w1, _w2 = len(word1), len(word2)
        s= ""
        for i in range((max(_w1, _w2))):
            if i< _w1:
                s +=word1[i]
            if i < _w2:
                s +=word2[i]
            
        return s