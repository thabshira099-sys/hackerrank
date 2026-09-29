def pairs(k, arr):  
    arrset=set(arr)
    count =0
    for i  in arr:
        if i+k in arrset:
            count+=1
    return count