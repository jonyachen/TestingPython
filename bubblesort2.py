# Bubble sort that follows FSM 1 geared towards FPGA versions
myList = [2, 5, 1, 4, 3]

def bubblesort(list):
    max = len(list) - 1
    counter = 0
    i = 0
    j = i + 1
    
    while (counter != (max - 1)):
        a = list[i]
        b = list[j]
        
        if (a > b):
            list[i] = b
            list[j] = a
            counter = 0
        else:
            counter = counter + 1
        if (j == max):
            max = max - 1
            i = 0
            j = i + 1
        else:
            i = i + 1
            j = j + 1

    return list

print bubblesort(myList)
