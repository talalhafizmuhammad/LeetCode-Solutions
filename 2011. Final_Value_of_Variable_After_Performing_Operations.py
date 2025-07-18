class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in operations:
            if i.upper() == '--X' or i.upper() == 'X--':
                res -= 1
            elif i.upper() == '++X' or i.upper() == 'X++':
                res += 1
        return res
