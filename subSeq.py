"""
Docstring for subSeq
"""

class Solution:
    def sub(self, s:String, t:String):


        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i+=1

        return i == len(s)