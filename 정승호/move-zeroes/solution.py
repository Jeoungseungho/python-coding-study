class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
        i, j = 0, 0
        
        for index in range(len(nums)):
            if nums[index] == 0:
                j += 1
            else:
                nums[index], nums[i] = nums[i], nums[index]
                i += 1
        
        
