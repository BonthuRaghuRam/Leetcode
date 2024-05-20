Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

Python Program

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre

or  

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        for i in range(len(first_str)):
            for j in range(1, len(strs)):
                curr_str = strs[j]
                if first_str[:i+1] != curr_str[:i+1]:
                    return first_str[:i]
        return first_str
