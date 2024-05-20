class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for i in range(len(s)-1):
            a=ord(s[i])
            b=ord(s[i+1])
            sum+=abs((a-b))
        return sum
