from asyncio.windows_events import NULL


matrixSize = int(input("Your Matrix size: "))
matrix = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
for i in range(0, matrixSize):
    line = input("Input line in Matrix: ")
    for j in range(0, matrixSize):
        matrix[i][j] = line.split(' ')[j]

right = 0
up = 1
left = 2
down = 3

print(matrix)
arr = []
minLength = float("inf")
print(minLength)
bestRoute = []

def findPath( i = 0, j = 0, prevMove = NULL):
    if ( j + 1 < matrixSize and prevMove != left):   # Move Right
        if (matrix[i][j+1] != '0'):
            arr.append("E")
            print(i, j+1)
            findPath( i, j + 1, right)
            arr.pop()

    if ( i - 1 >= 0 and prevMove != down):   # Move Up
        if (matrix[i - 1][j] != '0'):
            arr.append("N")
            print(i-1, j)
            findPath( i - 1, j, up)
            arr.pop()

    if ( j - 1 >= 0 and prevMove != right):   # Move Left
        if (matrix[i][j - 1] != '0'):
            arr.append("W")
            print(i, j-1)
            findPath( i, j - 1, left)
            arr.pop()
    
    if ( i + 1 < matrixSize and prevMove != up):   # Move Down
        if (matrix[i + 1][j] != '0'):
            arr.append("S")
            print(i+1, j)
            findPath( i + 1, j, down)
            arr.pop()

    if (i == matrixSize - 1 and j == matrixSize -1):    # reach the destination
        if (len(arr) < minLength):
            bestRoute = arr[:]
            print(bestRoute)
            return bestRoute


    



bestRoute = findPath()
print(bestRoute)
            
    

