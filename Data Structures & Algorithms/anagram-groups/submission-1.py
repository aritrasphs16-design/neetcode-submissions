class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=len(strs)
        dct={}
        for item in strs:
            count=[0]*26
            for rec in item:
                count[ord(rec)-ord('a')]+=1
            count=tuple(count)
            if count not in dct:
                dct[count]=[]
                dct[count].append(item)
            else:
                dct[count].append(item)
        return list(dct.values())

        