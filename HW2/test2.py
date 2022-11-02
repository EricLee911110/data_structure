class treeNode():
    def __init__(self, data=None, left=None, right=None, height=0, balance=0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height
        self.balance = balance

    def create_copy(self):
        copy = treeNode(self.data, self.left, self.right, self.height, self.balance)
        return copy

class AVLtree():
    def getHeight(self, node):
        if node == None:
            return -1
        else:
            return node.height

    def RRrotation(self, z):
        y = z.right
        t = z.right.left

        y.left = z
        z.right = t
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) +1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) +1

        return y

    def LLrotation(self,z):
        y = z.left
        t = z.left.right

        y.right = z
        z.left = t
        z.height = max(self.getHeight(z.left), self.getHeight(z.right)) +1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) +1

        return y


    def appendNode(self, node, data):
        if node == None:
            # print("new node")
            return treeNode(data)
        elif data < node.data:
            # print("smaller")
            node.left = self.appendNode(node.left, data)
        else:
            # print("greater")
            node.right = self.appendNode(node.right, data)

        # get height
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) +1 
        
        # perform rotations
        balance = self.getBalance(node)

        if balance < -1:
            if data < node.right.data:
                #print("RL")
                operations.append("RL")
                node.right = self.LLrotation(node.right)
                return self.RRrotation(node)           
            else:
                #print("RR")
                operations.append("RR")
                return self.RRrotation(node)
        if balance > 1:
            if data < node.left.data:
                #print("LL")
                operations.append("LL")
                return self.LLrotation(node)
            else:
                #print("LR")
                operations.append("LR")
                node.left = self.RRrotation(node.left)
                return self.LLrotation(node)

        return node

    def getBalance(self, node):
        if node == None:
            return 0
        else:
            return self.getHeight(node.left) - self.getHeight(node.right)

    def getMinNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def deleteNode(self, node, data):
        if node == None:
            return node
        elif data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:   # they are equal
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            
            
            # the node got deleted have two children?
            temp = self.getMinNode(node.right)
            node.data = temp.data
            node.right = self.deleteNode(node.right, temp.data)

        if root is None:
            return root

        

        # get height
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) +1 
    
        
        # perform rotations
        if self.getBalance(node) > 1:
            #print("was here")
            if self.getBalance(node.left) > 0:
                #print("LL") # R0 R1
                operations.append("R1")
                return self.LLrotation(node)
            elif self.getBalance(node.left) == 0:
                #print("LL") # R0 R1
                operations.append("R0")
                return self.LLrotation(node)
            else:
                #print("LR") # R-1
                operations.append("R-1")
                node.left = self.RRrotation(node.left)
                return self.LLrotation(node)
                
        if self.getBalance(node) < -1:
            #print("was here here")
            if self.getBalance(node.right) < 0:
                #print("RR") # R0 #R-1
                operations.append("R-1")
                return self.RRrotation(node)
            elif self.getBalance(node.right) == 0:
                #print("RR") # R0 #R-1
                operations.append("R0")
                return self.RRrotation(node)
            else:
                #print("RL") # R1
                operations.append("R1")
                node.right = self.LLrotation(node.right)
                return self.RRrotation(node)

        return node

        
    def postOrder(self, node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=" ")

    def inOrder(self, node):
        if node == None:
            return
        self.inOrder(node.left)
        resultTree.append(node.data)
        self.inOrder(node.right)
        


    def postOrderHeight(self, node):
        if node == None:
            return
        self.postOrderHeight(node.left)
        self.postOrderHeight(node.right)
        #print(f'Height of Node {node.data} is: {node.height}')

    def postOrderBalance(self, node):
        if node == None:
            return
        self.postOrderBalance(node.left)
        self.postOrderBalance(node.right)
        #print(f'Balance of Node {node.data} is: {node.balance}')

    
myTree = AVLtree()
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
    root = myTree.appendNode(root, num)
    #print(f'Now processing number: {num}')

#myTree.postOrder(root)

for command in delete_inputs:
    operation = command.split(' ')[0]
    num = int(command.split(' ')[1])
    #print(f'Now processing number: {num}')
    if operation == "I":
        #print("appending")
        myTree.appendNode(root, num)
    if operation == "D":
        #print("delete")
        myTree.deleteNode(root, num)

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

