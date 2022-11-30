inputs = [21, 24, 28, 15, 20, 19, 30, 41, 20, 28, 13, 12, 33, 25, 7]


def bubbleSort(arr, bubbleSwapCount, test):
    finish = True
    for i in range(len(inputs) - 1):
        if arr[i] > arr[i+1]:

            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            finish = False

            # tracking how many times we have swaped
            bubbleSwapCount += 1
            if bubbleSwapCount == 5 and test == True:
                #print(arr[i + 1], arr[i])
                return arr[i], arr[i + 1], arr
            


    if finish == True:
        return arr
    else:
        return bubbleSort(arr, bubbleSwapCount, test)

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

def select(arr, current_idx):
    smallest_num = float("inf")
    smallest_num_idx = 0

    for i in range(current_idx,len(arr)):
        if arr[i] < smallest_num:
            smallest_num = arr[i]
            smallest_num_idx = i

    return smallest_num, smallest_num_idx

def selectionSort(arr, selectCount):
    for i in range(len(arr)):
        # select smallest, then swap
        smallest_num, smallest_num_idx = select(arr, i) 
        #print(smallest_num, smallest_num_idx)
        arr[smallest_num_idx] = arr[i]
        arr[i] = smallest_num

        selectCount += 1
        if selectCount == 5:
            return smallest_num, arr 

bubbleSwap1, bubbleSwap2, bubbleResult = bubbleSort(inputs[:], 0, True)
#print(bubbleSwap1, bubbleSwap2, bubbleResult)

# why 1? Because the first element in the array will be added into sorted_list no matter what, and that counts as a step
insertionResult = insertionSort(inputs[:], 1)
#print(insertionResult)

select1, selectionResult = selectionSort(inputs[:], 0)
#print(select1, selectionResult)

final_sorted_list = bubbleSort(inputs[:], 0, False)

print("Bubble: ", end="")
print(f'{bubbleSwap1}, {bubbleSwap2};', end="")
for i in range(len(bubbleResult)):
    print(f' {bubbleResult[i]}', end="")

print()
print("Insertion:", end="")
for i in range(len(insertionResult)):
    print(f' {insertionResult[i]}', end="")

print()
print(f'Selection: {select1};', end="")
for i in range(len(selectionResult)):
    print(f' {selectionResult[i]}', end="")

print()
for i in range(len(final_sorted_list) - 1):
    print(f'{final_sorted_list[i]} ', end="")
print(final_sorted_list[len(final_sorted_list) - 1])