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
        node.balance = self.getHeight(node.left) - self.getHeight(node.right)

        if node.balance < -1:
            if data < node.right.data:
                print("RL")
                operations.append("RL")
                node.right = self.LLrotation(node.right)
                return self.RRrotation(node)           
            else:
                print("RR")
                operations.append("RR")
                return self.RRrotation(node)
        if node.balance > 1:
            if data < node.left.data:
                print("LL")
                operations.append("LL")
                return self.LLrotation(node)
            else:
                print("LR")
                operations.append("LR")
                node.left = self.RRrotation(node.left)
                return self.LLrotation(node)

        return node

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
            else:
                # the node got deleted have two children
                pass

        # get height
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) +1 
        
        # perform rotations
        node.balance = self.getHeight(node.left) - self.getHeight(node.right)

        if node.balance < -1:
            if data < node.right.data:
                print("D-RL")
                operations.append("D-RL")
                node.right = self.LLrotation(node.right)
                return self.RRrotation(node)           
            else:
                print("D-RR")
                operations.append("D-RR")
                return self.RRrotation(node)
        if node.balance > 1:
            if data < node.left.data:
                print("D-LL")
                operations.append("D-LL")
                return self.LLrotation(node)
            else:
                print("D-LR")
                operations.append("D-LR")
                node.left = self.RRrotation(node.left)
                return self.LLrotation(node)

        return node

        
    def postOrder(self, node):
        if node == None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data, end=" ")


    def postOrderHeight(self, node):
        if node == None:
            return
        self.postOrderHeight(node.left)
        self.postOrderHeight(node.right)
        print(f'Height of Node {node.data} is: {node.height}')

    def postOrderBalance(self, node):
        if node == None:
            return
        self.postOrderBalance(node.left)
        self.postOrderBalance(node.right)
        print(f'Balance of Node {node.data} is: {node.balance}')

    
myTree = AVLtree()
root = None
inputs = [63,9,19,27,18,70,95,99]
delete_inputs = [27, 5, 53, 99, 53]
operations = []
for num in inputs:
    root = myTree.appendNode(root, num)
    print(f'Now processing number: {num}')
    myTree.postOrderHeight(root)
    print()
    myTree.postOrderBalance(root)
    print()

myTree.postOrder(root)
print()
for operation in operations:
    print(operation, end=" ")

