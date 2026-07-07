# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode |None:
        # empty or not check   
        if not nums:
            return None

        # binary tree- break to 2
        mid=len(nums)//2
        # set it to the root
        root=TreeNode(nums[mid])

        # till the mid
        root.left=self.sortedArrayToBST(nums[:mid])
        # everything after the mid
        root.right=self.sortedArrayToBST(nums[mid+1:])

        return root