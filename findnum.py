#%%
mylist = [1,2,3,4,5,6,7]
target = 12

def findnum(mylist, target):
    low, high = 0, len(mylist) -1

    while (low < high):
        if mylist[low] + mylist[high] > target:
            high -= 1
        elif mylist[low] + mylist[high] < target:
            low += 1
        else:
            ans = (mylist[low], mylist[high])
            return ans
    return None

a = findnum(mylist, target)
    



#%%
