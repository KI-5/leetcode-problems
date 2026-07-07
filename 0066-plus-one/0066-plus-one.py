class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # last should get a +1
        # if it's 2 digits then can't should be separate
        for i in range(len(digits) - 1, -1, -1):
            # start, stop because the last is 0 so should be that and the one behind
            if digits[i]<9:
                digits[i]+=1
                return digits
            
            digits[i]=0
            # last digit as 0

        return [1]+digits
        # carry over 1 for each loop