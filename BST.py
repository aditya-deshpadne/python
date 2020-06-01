"Binary serch tree"

class Node:
        
    def __init__(self,data,right,left):
        self.data=data
        self.left=left
        self.right=right    
    



def main():
    arr = [ 2, 1, 9, 11, 0, 14 ]
    root = Node(arr[0],None,None)
    #print(root.data,root.left,root.right)
    for x in range(1,len(arr)):
        insertNode(root,arr[x])
    printInorder(root)


def insertNode(node,data):
    
    while(node != None):
        prev=node
        #print(node.data)
        if (data > node.data):
            node=node.right
        elif (data < node.data):
            node=node.left

    if (data > prev.data):
        prev.right = Node(data,None,None)
    else:
        prev.left = Node(data,None,None)

def printInorder(node):
    if(node == None):
        return
    printInorder(node.left)
    print(node.data,end =" ")
    printInorder(node.right)
    
    
main()    