#Bubble sort with while loop then while loop - more geared towards hardware with startAddr and numElements/some register stores
myList = [0, 0, 0, 0, 5, 2, 1, 4, 3, 1, 3, 2]


def bubblesort(list):
    startAddr = 4 #given
    numElements = 5 #given
    max = (startAddr + numElements) - 1
    sorted = False


    while not sorted:
        sorted = True
        i = startAddr
        a = list[startAddr] #or i
        while (i < max):
            b = list[i + 1]
            if a > b: # swap
                list[i + 1] = a
                list[i] = b
                sorted = False
            
            maxReg = a if (not sorted) else b #stores proper values in max/min regs
            minReg = b if (not sorted) else a
        
            i = i + 1
            a = maxReg
            #print list # for debugging
    return list

print bubblesort(myList)