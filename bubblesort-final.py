#Bubble sort with while loop then while loop - final version
myList = [0, 0, 0, 0, 5, 2, 1, 4, 3, 2, 6]


def bubblesort(list):
    startAddr = 4 #given
    numElements = 4 #given
    max = (startAddr + numElements) - 1
    sorted = False

    while not sorted:
        sorted = True
        i = startAddr
        a = list[startAddr] #or i
        while (i <= max):
            b = list[i + 1]
            maxSel = 0 if (a > b) else 1 #output of comparator
            minSel = 1 if (a > b) else 0 #output of comparator
            maxReg = a if (maxSel == 0) else b #the maximum number is stored in maxReg
            minReg = a if (minSel == 0) else b #the minimum number is stored in minReg
            list[i] = minReg
            if (a > b):
                sorted = False
            i = i + 1
            a = maxReg
            if (i >= max):
                list[i] = maxReg
                i = i + 1

    #print list # for debugging
    return list

print bubblesort(myList)