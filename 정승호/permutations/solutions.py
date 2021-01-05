class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
 
        def dfs(nums, path, result):
            if not nums:
                result.append(path)

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path+[nums[i]], result)
            
        dfs(nums, [], result)
        return result
    
