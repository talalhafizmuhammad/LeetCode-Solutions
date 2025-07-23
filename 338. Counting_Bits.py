class Solution(object):
    def countBits(self, n):
        count = 0
        myList = [0] * (n + 1)
        count = 0

        for i in range(n+1):
            count = 0
            num = (bin(i))
            for j in num:
                if j == '1': count += 1
            myList[i] = count
        return myList
