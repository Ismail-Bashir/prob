"""
Docstring for reverse words in string
"""


class Solution:
    def rev(self, s: String):

        newList = s.split()

        myList = []


        for i in range(len(s)-1, -1, -1):
            myList.append(newList[i])

        return " ".join(myList)