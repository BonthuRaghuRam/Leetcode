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

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        q = deque()
        q.append((0, 0))
        rev = False

        while q:
            tres = []
            for _ in range(len(q)):
                x, y = q.popleft()
                tres.append(mat[x][y])
                if y == 0 and x + 1 < m:
                    q.append((x + 1, y))
                if y + 1 < n:
                    q.append((x, y + 1))
            if rev:
                res += tres[::-1]
            else:
                res += tres
            rev = not rev
        return res
