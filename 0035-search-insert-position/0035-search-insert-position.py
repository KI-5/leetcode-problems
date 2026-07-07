class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # target found= return index
        # not= possible index
        # return bisect.bisect_left(nums, target)

        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                # Target is in the right half
                left=mid+1
            else:
                # Target is in the left half
                right=mid-1
            
        return left