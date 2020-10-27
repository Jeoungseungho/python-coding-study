class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_index = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] + i >= current_index:
                current_index = i
        return current_index == 0
