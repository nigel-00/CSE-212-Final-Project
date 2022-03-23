# Trees (Binary Search Trees)
A Binary Search Tree is a hierarchial form of data structure that follows these rules:
1. 1 root node - the ancestor of all the nodes in the tree.
2. Each node has a maximum of two children. 
3. Each node except the root has only one parent and a node cannot be its own parent.
4. A Binary Search Tree by definition has distinct keys and duplicates in binary search tree are not allowed.
## Terminology 
---------------
* Node - It is any structure that holds data. I like to think of a node as a container of data / key .
* Root  - The topmost node in the tree. It is the only mode from which all other nodes come from.
* Parent node - a node that has connected nodes.
* Child node - a node connected to the parent.
* Leaf  -a node that resides in the last level of a binary tree and  doesn't have any children. Its left and right children are null.
* Sub-tree - a sub-tree of a tree is a tree with its nodes being a descendant of some other tree. The nodes to the left and right of any parent node form a subtree.
* **NB** - Since the parent or child nodes are also nodes themselves, each node will hold a reference to a right and left node even if the node does not exist.

![Binary Search Tree](https://res.cloudinary.com/practicaldev/image/fetch/s--od-naD9n--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/975/1%2APWJiwTxRdQy8A_Y0hAv5Eg.png)

## Binary Search Tree operations
------------------
### Building a Binary Tree Node 
------------------
Since a node is a container for data and holds references to other nodes. Being a binary tree node, these references are to the left and the right children. Initially the left and right children are none. Data refers to data that will be contained in the node to establish a parent to children relationships accoriding to the rules of Binary Search Trees.

```python 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right  = None
```
You can simply create a new node by coding:
```python 
new_node = Node(8)
```
### Building a Binary Search Tree
------------------ 
The Binary Search Tree should hold a reference to its own root node.
```python  
class BinarySearchTree:
    def __init__(self):
        self.root  =  None
```
### Inserting into a Binary Search Tree 
-------------------
There are many ways of inserting into a BST. I will show an example of inserting using a while loop and provide a question to solve the same insertion question using recursion. The comments on the code will help you understand a step by step guide to inserting a node into a BST.
```python 
def insert(self, data):
        #Create a new node  
        new_node  = Node(data)
        #First check if the root node is none 
        if self.root is None:
            # set the new node to be the root node
            self.root = new_node 
            return 
        #keep track of the current node we are working on start from the root 
        current =  self.root
        #Loop through the tree 
        while current is not None:
            #Remove duplicates
            if current.data == new_node.data:
                return "No duplicates allowed!"
            #Insert new node on the left
            if new_node.data < current.data:
                #Check if there is an open spot to insert 
                if current.left is None:
                    #insert the new node in that empty spot 
                    current.left  = new_node
                    return 
                else:
                    #move current to the next node 
                    current = current.left
            #Insert a new node on the right 
            else:
                #Do the same thing on the right side if data is greater than current node 
                if current.right is None:
                    current.right = new_node
                    return 
                else:
                    #move current to the next node 
                    current = current.right
```
### Checking if the Binary Search Tree contains a value/ data 
----------------------
The insert method organizes data in a specific way, the same procedure is followed to find the data/ value. In this implementation, we will simply return True if it was found or False if the data was not found.
```python 
def contains(self, data):
        #Check if the root node is none 
        if self.root is None:
            return False
        #keep track of the current node you are working on 
        current = self.root 
        #Loop through the tree
        while current is not None:
            #check on the left side of the tree 
            if data < current.data:
                current = current.left
            #check on the right side of the tree
            elif data > current.data:
                current = current.right
            #return true if the node is in the tree 
            else:
                return True 
        #return false if its not 
        return False

```
### Finding the minimun and maximum value of a BST 
-------------------
The process of finding the minimum and maximun vale is very similar. If you are now comfortable with the rules of Binary Search Trees, this will be easy for you. I will only implement the min value node method. You can follow the same step to do the max value node.
```python
  def min_value_node(self, current_node):
        #Loop through the left tree 
        while current_node.left is not None:
            #move down the left tree side 
            current_node = current_node.left
        #return the last node on the left side of the tree
        return current_node
```
### Traversing a Binary Search Tree 
----------------
In inorder traversal, you visit the left sub-tree, the parent node, and finally the right sub-tree. There are other orders of traversing the BST such as pre-order, post-order traversal. The implementation is similar as long as you understand which side to visit first.

```python 
 def inorder(self, root_node): 
        # Start from the root node 
        current = root_node 
        # Return if the tree is empty 
        if current is None: 
            return 
        # recursively call the inorder method by moving to the next node on the left side 
        self.inorder(current.left)
        #print data everytime if finds a node 
        print(current.data) 
        # Do the same thing on the right
        self.inorder(current.right) 
    
```
### Finding height of a Binary Search Tree 
---------------
The implementation is similar to the inorder traversal in the sense that we visit the all the nodes in the tree. The difference is that with getting the height, we count the nodes on the left side and right side and then compare which side is greater than the other. The side with the highest height contains the maximum height of the tree.
```python 
def get_height(self, root_node):
    # Start from the root node 
    current = root_node 
    #Initialize the count variable 
    count  = 0
    # return o if the tree is empty 
    if current is None: 
        return count
    else:
        #call the left and right side recursively
        left = self.get_height(current.left)
        right = self.get_height(current.right)
        #Compare left and right side 
        if left > right:
            left += 1
            #return the max number of nodes on the left side if above condition is met
            return left
        else:
            right +=1
            #return the maximum number of nodes on the right side if the condition is met
            return right
```
## Big O Notation

| BST Operation  | Description                | Peformance     |
| :---:          |     :----:                 |         :---:  |
| Insert(value ) | Insert a value into a tree | O(log n)       |
| contains(value)| If a value is the tree.    | O(log n)       | 
| Traversing     | Visit all node in tree     | O(n)           |
| Height         | Get tree height            | O(n)           |
| empty()        | Return if root is empty    | O(1)           |
| size()         | Returns size of BST        | O(1)           |

**NB** - Inserting in a BST takes logarithmic time because we have to recursively search the subtrees to find the next available spot. Checking if the tree contains a value also happens in logarithmic time because we have to recursively search the subtrees to find the value. Getting the height and traversing the tree is O(n) because we have to recursively traverse the left subtree and then the right subtree. 



## Problem to solve

----------
### Question  
-----------
Solve the insert method using recursion. There are two methods. One is inserting on the Binary Search Tree and the other is inserting on the node. The starting code is the method that inserts on the BST. Complete the method that inserts on the Node.
### Starting code
```python 
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
```
### Finish the insert_on_node method
```python 
def insert_on_node(self, data, node):
    
    #your code goes here
```
## Solution 
---------------------
**NB** - Comments in the code will help you understand the solution step by step.
```python 
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
            return "No duplicates allowed      
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BinarySearchTree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```

