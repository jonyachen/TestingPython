#Bubble sort that's a combo of 1 and 2. while and for loop geared towards FPGA version
myList = [5, 2, 1, 4, 3]

def bubblesort(list):
    max = len(list) - 1
    sorted = False
    i = 0
    j = i + 1
    
    while not sorted:
        sorted = True
        for j in range(0 , max): # or (0, length)
            a = list[i]
            b = list[j]
            if a > b:
                sorted = False
                list[i] = b
                list[j] = a
            i = i + 1
            j = j + 1
        if ( j == max):
            i = 0
            j = i + 1
        print list
    return list

#bubblesort(myList)
#print myList

print bubblesort(myList)

WRONG because for loop already iterates through everything automatically