class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        for i in strs[1:]:
            while not i.startswith(first):
                first=first[:-1]

            if not first:
                return ""
        return first