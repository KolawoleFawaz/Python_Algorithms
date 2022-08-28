#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist
bubbleSort([29,13,22,37,52,49,46,71,56])

