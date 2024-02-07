class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = {}
        intlist=[]
        for i in nums:
            tmp.setdefault(i,0)
            tmp[i]+=1

        tmp = sorted(tmp.items(), key=lambda item: item[1], reverse = True)

        for i in range(k):
            intlist.append(tmp[i][0])

        return intlist


   