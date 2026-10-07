class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            ordered = ''.join(sorted(word))
            if ordered not in res:
                res[ordered] = []
            res[ordered].append(word)

        return list(res.values())