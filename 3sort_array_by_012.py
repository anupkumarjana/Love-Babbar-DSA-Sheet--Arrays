#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        count0=0
        count1=0
        count2=0
        for i in range(len(arr)):
            if arr[i]==0:
                count0+=1
            if arr[i]==1:
                count1+=1
            if arr[i]==2:
                count2+=1
        i=0
        while count0>0:
            arr[i]=0
            i+=1
            count0-=1
        while count1>0:
            arr[i]=1
            i+=1
            count-=1
        while count2>0:
            arr[i]=1
            i+=1
            count-=1
