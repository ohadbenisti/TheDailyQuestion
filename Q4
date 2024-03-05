def isBalanced(arr):
    pos=0
    neg=0
    
    for i in arr:
        if(i>0):
            pos+=1
        else:
            neg+=1
        if(pos==neg):
            print(arr)
            return
        newArr=[0]*len(arr)
        ni=len(arr)-1
        for i in range(len(arr)):
            newArr[ni]=arr[i]
            ni-=1

    print(newArr)
    
test=[1,2,3,4,-1,-2,-3,-4]
isBalanced(test)

test=[1,2,3,4,-1,2,-3,-4]
isBalanced(test)
