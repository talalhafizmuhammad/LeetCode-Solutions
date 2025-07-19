class Solution(object):
    def removeSubfolders(self, folder):
       
        folder.sort()
        result = []
        
        for path in folder:
            if not result or not path.startswith(result[-1] + "/"):
                result.append(path)
        
        return result
