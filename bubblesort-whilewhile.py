#Bubble sort with while loop then while loop - geared towards hardware
myList = [5, 2, 1, 4, 3]

def bubblesort(list):
    max = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        i = 0
        while (i < max):
            a = list[i]
            j = i + 1
            b = list[j]
            if a > b: # swap
                list[i] = b
                list[j] = a
                sorted = False
            i = i + 1
            #print list # for debugging
    return list

print bubblesort(myList)