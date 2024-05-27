class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=[i for i in s.lower() if i.isalnum()]
        return s2==s2[::-1]
                
        
