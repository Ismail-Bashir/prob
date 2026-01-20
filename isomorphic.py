"""
Docstring for isomorphic
"""


class Solution:
    def iso(self, s:String, t:String):

        mapST, mapTS = {}, {}


        for c1, c2 in zip(s, t):
            if c1 in mapST and mapST[c1] != c2:
                return False
            if c2 in mapTS and mapTS[c2] != c1:
                return False
            
            mapST[c1]=c2
            mapTS[c2]=c1


        return True