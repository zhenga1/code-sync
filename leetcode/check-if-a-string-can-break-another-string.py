class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        def canBreak(dom, sub):
            # dom = dominant (the breaking string) (dictionary of distributions)
            # sub = submissive (the broken string) (dictionary of distributions)
            cumsumdum, cumsumsum = 0, 0
            for i in range(25, -1, -1): # start from z which is the largest letter
                cumsumdum += dom[i]
                cumsumsum += sub[i]
                if cumsumdum < cumsumsum: # there are more big chars then can be handled up to some letter
                    return False
            return True

        base = ord("a")
        dic_s1, dic_s2 = collections.defaultdict(int), collections.defaultdict(int)
        for c in s1:
            dic_s1[ord(c) - base] += 1
        for c in s2:
            dic_s2[ord(c) - base] += 1
        
        return canBreak(dic_s1, dic_s2) or canBreak(dic_s2, dic_s1)