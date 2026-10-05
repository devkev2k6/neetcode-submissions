class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for r in range(len(nums)):
            while nums[r]!=0:
                nums[l]=nums[r]
                l+=1
                nums[r]=0
