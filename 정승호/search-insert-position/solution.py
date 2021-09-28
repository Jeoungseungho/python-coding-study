class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start = 0
        if start == end:
            return 0 if target <= nums[0] else 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid -1
            else:
                start = mid + 1
        return mid if target < nums[mid] else mid + 1
            
