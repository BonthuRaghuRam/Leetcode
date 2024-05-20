class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        num=len(nums)
        for i in range(0,num):
            for j in range(i+1,num):
                if i<j:
                    if nums[i]==nums[j]:
                        count+=1
        return count
                        
        
