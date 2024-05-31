# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        temp = []
        temp.append(root)
        res = []
        while len(temp) > 0:
            sum=0
            for i in range(len(temp)):
                if temp[0].left is not None:temp.append(temp[0].left)
                if temp[0].right is not None:temp.append(temp[0].right)
                sum+=temp[0].val
                temp.pop(0)
            # sum+=maxi
            res.append(sum)
        max1=res[0]
        max2=0
        for i in range(len(res)):
            if res[i]>max1:
                max2=i
                max1=res[i]
            
        return max2+1    
