class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = {}
        for i in strs:
            sortedstr = ''.join(sorted(i))
            if sortedstr not in tmp:
                tmp[sortedstr] = [i]
            else:
                tmp[sortedstr].append(i)
        return tmp.values()
