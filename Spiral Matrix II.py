class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for i in range(n)]
        top=0
        left=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        cnt=1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                matrix[top][i]=cnt
                cnt+=1
            top+=1
            
            for i in range(top,bottom+1):
                matrix[i][right]=cnt
                cnt+=1
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=cnt
                    cnt+=1
                bottom-=1

            if left<=right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=cnt
                    cnt+=1
                left+=1


        return matrix
        
