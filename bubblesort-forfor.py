#Bubble sort with for loop then for loop
myList = [5, 2, 1, 4, 3]

def bubblesort(list):

    for i in range(0, len(list)):
        for j in range(0, len(list)-1):
            if list[j] > list[j + 1]:
                temp = list[j + 1]
                list[j + 1] = list[j]
                list[j] = temp
    return list

print bubblesort(myList)