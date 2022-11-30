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
                print(arr[i + 1], arr[i])
                return arr[i + 1], arr[i], arr
            


    if finish == True:
        return arr
    else:
        return bubbleSort(arr, bubbleSwapCount)


bubbleSwap1, bubbleSwap2, bubbleResult = bubbleSort(inputs, 0)
print(bubbleResult)

