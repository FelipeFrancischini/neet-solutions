class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        restant = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            restant[sortedS].append(s)
        return list(restant.values())
