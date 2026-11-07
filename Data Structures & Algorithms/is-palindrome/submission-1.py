class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=s.split()
        s=''
        for item in lst:
            for x in item:
                if x.isalpha()==True or x.isdigit():
                    s+=x.lower()
        s1=s[::-1]
        print(s)
        print(s1)
        if s==s1:
            return True
        else:
            return False

        