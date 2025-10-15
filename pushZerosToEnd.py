#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        n = len(arr)
        index = 0
        
        for i in range(n):
            if arr[i] != 0:
                arr[index] = arr[i]
                index +=1
        while index < n:
            arr[index] = 0
            index += 1
            
        return arr
        
        
arr = [0,3,0,5,0,4]
ob = Solution()
result =  ob.pushZerosToEnd(arr)
# print(result)
