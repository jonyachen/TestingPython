#Bubble sort with while loop then for loop
myList = [5, 2, 1, 4, 3]

def bubblesort(list):
    max = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(max):
            if list[i] > list[i + 1]:
                sorted = False
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp #Another way to swap: list[i], list[i+1] = list[i+1], list[i]
    return list

print bubblesort(myList)