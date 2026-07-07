from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted
        if sorted(s)==sorted(t):
            return True
        else:
            return False
        return True if sorted(s)==sorted(t) else False

        # Counter
        return True if Counter(s)==Counter(t) else False

        # with for 
        if len(s)!=len(t):
            return False
    
        countS={}
        countT={}

        for char in s:
            if char in countS:
                countS[char]+=1
            else:
                countS[char]=1

        for char in t:
            if char in countT:
                countT[char]+=1
            else:
                countT[char]=1
        return countS==countT