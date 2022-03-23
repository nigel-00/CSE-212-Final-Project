

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right  = None

class BinarySearchTree:
    def __init__(self):
        self.root  =  None
    
    def insert_on_bst(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BinarySearchTree.Node(data)
        else:
            self.insert_on_node(data, self.root)  # Start at the root

    def insert_on_node(self, data, node):
            
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = BinarySearchTree.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self._insert(data, node.left)
            # No duplicates allowed in Binary Search Trees
            elif data == node.data:
                return "No duplicates allowed"     
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = BinarySearchTree.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.
                    self._insert(data, node.right)
#Initialize the binary tree 
my_tree = BinarySearchTree()
#Test cases to help you see if your code worked 
my_tree.insert_on_bst(8)  
my_tree.insert_on_bst(5)
my_tree.insert_on_bst(12)
my_tree.insert_on_bst(2)
my_tree.insert_on_bst(7) 
#Print all the nodes inserted in the tree 
for i in my_tree:
    print(i)
