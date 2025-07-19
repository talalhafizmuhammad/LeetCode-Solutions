class Solution(object):
    def findTheDifference(self, s, t):
        myList = []
        sort1 = ''.join(sorted(s))
        sort2 = ''.join(sorted(t))
        lst1 = list(sort1)
        lst2 = list(sort2)
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return lst2[i]
        return lst2[-1]
