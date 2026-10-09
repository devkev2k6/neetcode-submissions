class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        leftSum=0
        for i in range(nums):
            rightSum=total - nums[i] - leftSum
            if leftSum==rightSum:
                return i
            leftSum+=rightSUm
        return -1
        