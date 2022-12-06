
class TreeNode():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree():
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Function to insert a node
    def insert_node(self, root, key):

        # Find the correct location and insert the node
        if root == None:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                #print("LL")
                operations.append("LL")
                return self.rightRotate(root)
            else:
                #print("LR")
                operations.append("LR")
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                #print("RR")
                operations.append("RR")
                return self.leftRotate(root)
            else:
                #print("RL")
                operations.append("RL")
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        #print(f'Height for node {root.key} is: {root.height}')

        return root

    # Function to delete a node
    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                print("poke")
                myTree.postOrder(temp)
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) == 0:
                operations.append("R0")
                #print("LL") # R0 R1
                return self.rightRotate(root)
            elif self.getBalance(root.left) > 0:
                #print("LL") # R0 R1
                operations.append("R1")
                return self.rightRotate(root)    
            else:
                #print("LR") # R-1
                operations.append("R-1")
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if self.getBalance(root.right) < 0:
                #print("RR") # R0 #R-1
                operations.append("R-1")
                return self.leftRotate(root)
            elif self.getBalance(root.right) == 0:
                print("RR ", root.key) # R0 #R-1
                print("poke: ")
                myTree.postOrder(root)
                operations.append("R0")
                return self.leftRotate(root)
            else:
                #print("RL") # R1
                operations.append("R1")
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            #print("I run here")
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(f'{root.key}', end="")
    
    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        resultTree.append(node.key)
        self.inOrder(node.right)
        

myTree = AVLTree()
root = None

delete_inputs = []

line = input()
inputs = list(map(int, line.split(',')))


while True:
    line = input()
    if line == '':
        break
    delete_inputs.append(line)




operations = []
for num in inputs:
    root = myTree.insert_node(root, num)
    myTree.postOrder(root)
    print("")

#myTree.postOrder(root)

for command in delete_inputs:
    operation = command.split(' ')[0]
    num = int(command.split(' ')[1])
    #print(f'Now processing number: {num}')
    if operation == "I":
        #print("appending")
        myTree.insert_node(root, num)
    if operation == "D":
        #print("delete")
        myTree.delete_node(root, num)

    myTree.postOrder(root)
    print("")

    #myTree.postOrder(root)
    #print()

#print("result: \n")
#print reuslt
resultTree = []
myTree.inOrder(root)
#print(resultTree)
for i in range(len(resultTree)):
    if i == len(resultTree) -1:
        print(str(resultTree[i]))
    else:
        print(str(resultTree[i]), end=" ")

print(str(len(operations)))

for i in range(len(operations)):
    if i == len(operations) -1:
        print(str(operations[i]))
    else:
        print(str(operations[i]), end=",")