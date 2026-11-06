class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[]
        postfix=[]
        res=[]
        prod=1
        for i in range(n):
            prod*=nums[i]
            prefix.append(prod)
        prod=1
        for i in range(n-1,-1,-1):
            prod*=nums[i]
            postfix.append(prod)
        postfix=postfix[::-1]
        for i in range(n):
            if i==0:
                res.append(1*postfix[i+1])
            elif i==n-1:
                res.append(1*prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res


        