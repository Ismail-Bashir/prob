"""
Docstring for palindrome
"""


class Solution:
    def isPalind(self, s:String):
        cleaned = []


        for i in range(len(s)):
            if s[i].isalnum():
                cleaned.append(s[i].lower())


        cleaned = ''.join(cleaned)


        return cleaned == cleaned[::-1]