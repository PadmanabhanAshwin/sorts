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
        self.sorted_list = []
        

sortobj = Sort(mylist = [2,1,3])

print(sortobj.bubblesort())

#%%
