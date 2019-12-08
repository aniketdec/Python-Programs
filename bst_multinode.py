class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
        self.nodes_in_left=0
        self.nodes_in_right=0
        self.count=1
def insert(root,node):
    if root is None:
        root=node
    else:
        if root.val<node.val:
            root.nodes_in_right+=1
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)
        elif root.val>node.val:
            root.nodes_in_left+=1
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
        else:
            root.count+=1
def inorder(root):
    if root:
        inorder(root.left)
        print "  ",root.val,"   ",root.count,"   ",root.nodes_in_left,"   ",root.nodes_in_right
        inorder(root.right)

root=Node(8)#Root Node
l=[3,6,1,7,7,4,10,7,14,14,13,1]
'''
                        Tree
                        8
                       / \
                      3   10
                     / \    \
                 (2)1   6    14(2)
                       /  \    /
                      4 (3)7 13
'''             
for i in l:
    node=Node(i)
    #print node.val
    insert(root,node)
    #print
def details_in_inorder():
    print "Value Count leftnodes rightnodes"
    inorder(root)
details_in_inorder()
