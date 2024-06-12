class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=""
        i=0
        if ch not in word:
            return word
        while i<len(word):
            if word[i]==ch:
                res+=word[:i+1]
                break
            i+=1
        return res[::-1]+word[i+1:]
        
