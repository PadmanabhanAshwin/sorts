#%%
text = "Madams"

def ispal(text):
    low = 0
    high = len(text) -1 
    pallbool = True
    while (low <= high):
        if text[low].lower() != text[high].lower():
            pallbool = False
            return pallbool
        low += 1
        high -=1
    return pallbool

ispal(text)

#%%
