inputs = [21, 24, 28, 15, 20, 19, 30, 41, 20, 28, 13, 12, 33, 25, 7]


def bubbleSort(arr, bubbleSwapCount):
    finish = True
    for i in range(len(inputs) - 1):
        if arr[i] > arr[i+1]:

            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            finish = False

            # tracking how many times we have swaped
            bubbleSwapCount += 1
            if bubbleSwapCount == 5:
                #print(arr[i + 1], arr[i])
                return arr[i], arr[i + 1], arr
            


    if finish == True:
        return arr
    else:
        return bubbleSort(arr, bubbleSwapCount)

def insert(arr, small_num_idx):
    finish = True

    for i in range(small_num_idx):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            finish = False

    if finish == True:
        return arr
    else:
        return insert(arr, small_num_idx)

    

def insertionSort(arr, insertCount):
    for i in range(len(arr) -1):
        if arr[i] > arr[i+1]:
            
            # insert to the right place
            arr = insert(arr, i + 1)
            insertCount += 1
            
            if insertCount == 5:
                #rint("step : ", insertCount)
                #print(arr)
                return arr
        else:
            insertCount += 1
            if insertCount < 6:
                pass
                #print("step : ", insertCount)
                #print(arr)

bubbleSwap1, bubbleSwap2, bubbleResult = bubbleSort(inputs[:], 0)
#print(bubbleSwap1, bubbleSwap2, bubbleResult)

# why 1? Because the first element in the array will be added into sorted_list no matter what, and that counts as a step
insertionResult = insertionSort(inputs[:], 1)
print(insertionResult)