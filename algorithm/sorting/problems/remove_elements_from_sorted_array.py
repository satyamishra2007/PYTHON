







class Solution:
    # @param A : list of integers
    # @return an integer


    def removeDuplicates_1(self,A):
        print(" Using extra List")
        res = []
        for i in A:
            if i not in res:
                res.append(i)
        print(res)
        return len(res)



    #Inplace update : T O(N) S O(1)
    def removeDuplicates(self, A):
        i=0
        j=1
        while(j<len(A)):
            if(A[i]==A[j]):
                j+=1
            else:
                i+=1
                A[i]=A[j]
        A=A[:i+1]
        print(A)
        return i+1


print(Solution().removeDuplicates([1,2,3,4,4,4,5,5]))
print(Solution().removeDuplicates_1([1,2,3,4,4,4,5,5]))