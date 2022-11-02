class treeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

user_input = input()
arr = user_input.split(" ")

root = treeNode()
root.data = int(arr[0])


def appendNode(node, num1):
    if num1 < node.data:
        #print("left")
        if node.left == None:
            node.left = treeNode()
            node.left.data = num1
            #print(num1)
        else:
            appendNode(node.left, num1)

    else:
        #print("right")
        if node.right == None:
            node.right = treeNode()
            node.right.data = num1
            #print(num1)
        else:
            appendNode(node.right, num1)

for i in range(1, len(arr)):
    appendNode(root, int(arr[i]))




# inorder
def printInorder(node):
    
    if node.left != None:
        printInorder(node.left)

    result.append(node.data)
    
    if node.right != None:
        printInorder(node.right)

# preorder
def printPreorder(node):
    
    result.append(node.data)

    if node.left != None:
        printPreorder(node.left)
    
    if node.right != None:
        printPreorder(node.right)

# postorder
def printPostorder(node):

    if node.left != None:
        printPostorder(node.left)
    
    if node.right != None:
        printPostorder(node.right)

    result.append(node.data)

result = []
printInorder(root)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(f'{result[i]} ', end='')

result = []
printPreorder(root)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(f'{result[i]} ', end='')

result = []
printPostorder(root)
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i])
    else:
        print(f'{result[i]} ', end='')