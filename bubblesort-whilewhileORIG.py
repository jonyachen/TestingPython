#Bubble sort with while loop then while loop - original
myList = [5, 2, 1, 4, 3]

def bubblesort(list):
    max = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        i = 0
        while (i < max):
            if list[i] > list[i + 1]: # swap
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
                sorted = False
            i = i + 1
    #print list # for debugging
    return list

print bubblesort(myList)