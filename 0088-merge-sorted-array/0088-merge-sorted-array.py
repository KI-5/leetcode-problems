class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # n1 has enough to accommodate what n2 has too
        # no need to trim the array
        # get the vals of n2 to the 0 vals in n1
        nums1[m:]=nums2
        nums1.sort()
        