class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r = []
        for i in sentences:
            r.append(len(i.split()))
        return max(r)        
        
