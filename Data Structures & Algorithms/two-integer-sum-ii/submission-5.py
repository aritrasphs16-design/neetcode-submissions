class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        ptr1=0
        ptr2=n-1
        for i in range(n):
            if numbers[ptr1]+numbers[ptr2]==target:
                ptr1+=1
                ptr2-=1
                return [ptr1,ptr2+2]
            elif numbers[ptr1]+numbers[ptr2]>target:
                ptr2-=1
            else:
                ptr1+=1

        