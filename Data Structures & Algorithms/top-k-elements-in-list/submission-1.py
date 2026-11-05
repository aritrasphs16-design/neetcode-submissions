class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         dct={}
         for num in nums:
            dct[num]=dct.get(num,0)+1
         n=len(nums)
         bucket=[[] for i in range(n+1)]
         for item,freq in dct.items():
            bucket[freq].append(item)
         res=[]
         for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res