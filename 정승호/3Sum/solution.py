class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            # 중복값 건너뛰기 
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 간격 좁히면서 sum 계산
            left, right = i+1, len(nums)-1
            while left < right:
                answer = nums[i] + nums[left] + nums[right]
                if answer < 0 :
                    left += 1
                elif answer > 0:
                    right -= 1
                else :
                    # 정답 및 스킵처리 
                    result.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return result
            
