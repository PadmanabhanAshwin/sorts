#%% 
# Sorting methods

class Sort():
    def __init__(self, mylist):
        self.list = mylist
    
    def bubblesort(self):
        mylist = self.list
        boolsort = False

        while not boolsort:
            boolsort = True
            for i in range(len(mylist) -1):
                if mylist[i] > mylist[i+1]:
                    temp = mylist[i+1]
                    mylist[i+1] = mylist[i]
                    mylist[i] = temp
                    boolsort = False
        self.sorted_list = mylist
        return self.sorted_list
    
    def selectionsort(self):
        mylist = self.list
        mincounter = 0
        for _ in range(0, len(mylist)):
            currentmin = mylist[mincounter]
            curr_ix = mincounter
            for i in range(mincounter + 1, len(mylist)):
                if mylist[i] < currentmin:
                    currentmin = mylist[i]
                    curr_ix = i 

            temp = mylist[mincounter]
            mylist[mincounter] = mylist[curr_ix]
            mylist[curr_ix] = temp
            mincounter += 1
        
        self.sorted_list = mylist
        return self.sorted_list
    
    def insertionsort(self):
        mylist = self.list
        print(mylist)

        for i in range(1, len(mylist)):
            for j in range(0, i):
                if mylist[i] < mylist[j]:
                    temp = mylist[i]
                    for k in range(i -1, j-1, -1):
                        mylist[k+1] = mylist[k]
                    mylist[j] = temp
                    print(mylist)
                    break
        return mylist

sortobj = Sort(mylist = [125123,39123 ,2123123, 124123511])
print(sortobj.insertionsort())

#%%


#%%
