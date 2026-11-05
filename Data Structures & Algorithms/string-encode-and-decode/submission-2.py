class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for i in range(len(strs)):
            s+=str(len(strs[i]))+'#'+strs[i]
        return s

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            n=int(s[i:j])
            res.append(s[j+1:j+1+n])
            i=j+1+n
        return res