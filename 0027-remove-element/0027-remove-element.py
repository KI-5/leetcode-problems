class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove val in nums
        # changing order is fine
        # have the array with the vLUES that aren't val at the start
        # RETURN the number of elements tht arent equal meaning k

        change=0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[change]=nums[i]
                change+=1
            

        return change