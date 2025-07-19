class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            t = ""
            for ch in s:
                t += chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
            s += t
        return s[k - 1]
