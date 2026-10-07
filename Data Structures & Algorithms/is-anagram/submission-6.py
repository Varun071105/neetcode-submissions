class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alf = [0] * 26
        for c in s:
            alf[ord(c) - ord('a')] += 1
        for c in t:
            alf[ord(c) - ord('a')] -= 1
        for c in alf:
            if c != 0:
                return False
        return True