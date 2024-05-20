class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum=0
        max=[]
        for i in accounts:
            for j in i:
                sum+=j
            max.append(sum)
            sum=0
        max.sort()
        return max[-1]
