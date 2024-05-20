class Solution:
    def defangIPaddr(self, address: str) -> str:
        b=address.replace(".","[.]")
        return b
        
