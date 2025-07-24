class Solution(object):
    def isAnagram(self, s, t):
        ans1 = list(s)
        ans2 = list(t)
        ans1.sort()
        ans2.sort()
        if len(ans1) != len(ans2):
            return False
        for i in range(len(ans1)):
            if ans1[i] != ans2[i]:
                return False
        return True
        
