class Solution:
    def minSteps(self, s: str, t: str) -> int:

        dict1 = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,
        }

        dict2 = {
            'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,
        }

        s = ''.join( sorted( s ) )
        t = ''.join( sorted( t ) )

        for char in s : dict1[char] += 1
        for char in t : dict2[char] += 1

        unique1 = 0
        unique2 = 0

        for key in dict1.keys() :

            diff = dict1[key] - dict2[key]

            if diff > 0 : unique2 += diff
            elif diff < 0 : unique1 -= diff

        return unique1 + unique2
    
# Beats 5.25% Runtime, 845ms
# Beats 20.99% Memory, 18.2mb