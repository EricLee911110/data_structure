
matrixSize = int(input(""))
matrix = [[0 for i in range(matrixSize)] for j in range(matrixSize)]
visited = matrix[:][:]
for i in range(0, matrixSize):
    line = input("")
    for j in range(0, matrixSize):
        matrix[i][j] = line.split(' ')[j]


right = 0
up = 1
left = 2
down = 3

arr = []
minLength = float("inf")

def findPath( bestRoutes = [], i = 0, j = 0, prevMove = -1):
    visited[i][j] = 1

    if (i == matrixSize - 1 and j == matrixSize -1):    # reach the destination
        if (len(arr) < minLength):
            bestRoutes.append(arr[:])
            visited[i][j] = 0           # when it reach the destination, the code stops here, so it mark the destination as visited. So in the next loop, it can't reach the destination.
            return bestRoutes
    
    else:
        if ( j + 1 < matrixSize and prevMove != left and visited[i][j+1] != 1):   # Move Right
            if (matrix[i][j+1] != '0'):
                arr.append("E")
                bestRoutes = findPath( bestRoutes, i, j + 1, right)
                arr.pop()

        if ( i - 1 >= 0 and prevMove != down and visited[i-1][j] != 1):   # Move Up
            if (matrix[i - 1][j] != '0'):
                arr.append("N")
                bestRoutes = findPath( bestRoutes, i - 1, j, up)
                arr.pop()


        if ( j - 1 >= 0 and prevMove != right and visited[i][j-1] != 1):   # Move Left
            if (matrix[i][j - 1] != '0'):
                arr.append("W")
                bestRoutes = findPath( bestRoutes, i, j - 1, left)
                arr.pop()

        if ( i + 1 < matrixSize and prevMove != up and visited[i+1][j] != 1):   # Move Down
            if (matrix[i + 1][j] != '0'):
                arr.append("S")
                bestRoutes = findPath( bestRoutes, i + 1, j, down)
                arr.pop()

    visited[i][j] = 0

    

    return bestRoutes


bestRoutes = findPath()

idx_shortestPath = 0
for i in range(0, len(bestRoutes)):
    if (len(bestRoutes[i]) < len(bestRoutes[idx_shortestPath])):
        idx_shortestPath = i

shortestPath = ""
for e in bestRoutes[idx_shortestPath]:
    shortestPath += str(e)

print(shortestPath)


    

