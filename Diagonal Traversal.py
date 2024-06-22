Approach I

class Solution:
    def matrixDiagonally(self,mat):
        a={}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                b=i+j
                if b not in a:
                    a[b]=[mat[i][j]]
                else:
                    a[b].append(mat[i][j])
                    
        c=[]
        for i in range(len(a)):
            if i%2 !=0:
                c.extend(a[i])
            else:
                c.extend((a[i])[::-1])
        return c

Approach II

from collections import deque
class Solution:
    def matrixDiagonally(self,mat):
        m,n=len(mat),len(mat[0])
        visited = [[False] * n for i in range(m)]
        res=[]
        q=deque()
        q.append((0,0))
        visited[0][0] = True
        rev=False
        while q:
            temp=[]
            for i in range(len(q)):
                x,y=q.popleft()
                temp.append(mat[x][y])
                if y==0 and x+1<m and not visited[x + 1][y]:
                    q.append((x+1,y))
                    visited[x + 1][y] = True
                if y+1<n and not visited[x][y + 1]:
                    q.append((x,y+1))
                    visited[x][y + 1] = True
            
            if rev:
                res+=temp[::-1]
            else:
                res+=temp[:]
            rev=not rev
        return res
