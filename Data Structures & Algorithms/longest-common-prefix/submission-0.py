class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        result = ""

        for i in range(len(smallest)):
            char = smallest[i]

            for word in strs:
                if word[i] != char:
                    return result

            result += char

        return result
