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

        

sortobj = Sort(mylist = [3123,2123141,12331, 1])
print(sortobj.selectionsort())

#%%


#%%
