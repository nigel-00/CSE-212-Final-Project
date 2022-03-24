# Linked List
 A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
 Linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

A linked list is represented by a pointer to the first node of the linked list. 
You can think of a linked list as a set of nested dictionaries.
I am going to demonstrate more how a doubly linked list works. If one understands a doubly linked list, it will be easy to understand the singly linked list.
## Doubly Linked List 
-----
* The singly linked list had a single pointer pointing to the next node. But a doubly linked list contains two pointers. One pointer points to the next node and one pointer to the previous node. Thus, a doubly linked list is a two-way chain.
* The purpose of a doubly linked list is to enable both-way traversal while still allowing non-contiguous memory storage. Just like a singly linked list, we need to have a starting pointer pointing to the first node. The last node in the list points to NULL.
### Every node in a doubly linked list has:
* Data
* Address of the next node
* Address of the previous node

## Terminology 
-----
* **Head** - The first node is called the head. If the linked list is empty, then the value of the head points to NULL. Head points to the first node in the list
* **Tail** - The last node is called the tail and it points to the last item. 
* **Node** - the node is a container. It is made up of the value/ data and the pointers. 
* **Prev** - It is a pointer pointing towards the previous node. For the first node, Prev points to NULL.

* **Next** - It links the current node to the next node in the linked list. The Next of the last node points towards NULL.

![Linked List](https://media.geeksforgeeks.org/wp-content/uploads/XorLinkedList.jpg)

A single node would look like this:

![Single Node]( https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRceZvlpV2cXOPfs8nHVXaqr0PfGsQGVinD2oHXy2FnnQyQ9v9jl_FprdUzQ-epRDOykRU&usqp=CAU)

## Creating a Doubly Linked List Node
```python
class Node:
    def __init__(self, value):
        #Node value 
        self.value = value 
        #Next pointer 
        self.next = None
        #Previous pointer
        self.prev = None 
```
## Creating Doubly Linked List class 
**NB** - The Node class is part of the Doubly Linked List.
```python 
class DoublyLinkedList:
    """The Node class is a sub class of the Doubly Linked Class"""
    class Node:
    def __init__(self, value):
        #Node value 
        self.value = value 
        #Next pointer 
        self.next = None
        #Previous pointer
        self.prev = None
    """The constructor of the Doubly Linked List class"""
    def __init__(self, value):
        #Create a new node 
        new_node = DoublyLinkedList.Node(value)
        #Point the head to the new node 
        self.head = new_node 
        #Point the tail to the ne node 
        self.tail = new_node 
        #Initial length of the List
        self.length =  1
    """You can create a method to print the values in the Linked list"""
    
    def print_list(self):
        #Start from the head 
        current = self.head
        #Loop through the linked list 
        while current is not None:
            #Print the value of current everytime you move
            print(current.value)
            #set current to the next node 
            current = current.next
```
## Big O Notation of Doubly Linked List Operations
------
| BST Operation         | Description                                   | Peformance     |
| :---:                 |     :----:                                    |         :---:  |
| Insert at head(value )| Insert a value at the head of a linked list   | O(1)           |
| Insert at tail(value) | If a value at the tail of a linked list       | O(1)           | 
| Insert after a node   | Visit all node in tree and insert after a node| O(n)           |
| Size                  | Get Linked list size                          | O(1)           |
| empty()               | Checks if the list is empty                   | O(1)           |

**NB** - Inserting and removing at either head or tail is O(1) becuase you are simply adjusting the pointers near the head or tail not the whole Linked list. However its different when inserting at a certain position in the Linked list because  you have to loop through the linked list to find the index and insert or remove after. That is O(n).

## Inserting into a Doubly Linked List
------
**NB**- The comments on code will help you undertand the steps.
* Inserting into a linked list only has an effect on the neighboring elements of the node being inserted.
* We are going to use pointers such as next, prev, head, and tail to connect the nodes together.
* We can insert at the head, in the middle and at the end of a Doubly Linked List.
* Removing in any place on a Doubly Linked list is similar to inserting
* I will provide a question to solve removing a value in the Linked List.
### Inserting and removing at the head of a Doubly Linked List 
-------
```python 
""""Inserting into a Douubly Linked List"""
def append_at_head(self,value):
        #Create a new node 
        new_node = DoublyLinkedList.Node(value)
        #Insert a node if the list is empty
        if self.head is None:
            #Point the head and tail to new node 
            self.head = new_node 
            self.tail = new_node 
            return 
        else: 
            #set the head to be the next of the new node 
            new_node.next = self.head
            #place the new node previous to the head 
            self.head.prev = new_node
            #point the head to the new node
            self.head = new_node 
        #Increase the length
        self.length += 1
        return 
"""Removing from a Doubly Linked List"""

def remove_at_head(self):
        #Check if the list is empty 
        if self.length == 0:
            return None
        #Variable keeping track of the current node 
        current = self.head
        #set head and tail to node if there is one item in the list
        if self.length == 1:
            self.head  = None 
            self.tail = None
        else:
            #set the head to the next node
            self.head = self.head.next 
            #set the previous of the new head to none 
            self.head.prev  = None 
            #set the next of current to None to break the connection
            current.next  = None
        #Keep track of the length of the list
        self.length -= 1
        return current.value

```
### Inserting in the middle of a Doubly Linked List after a given value.
-------
```python
def insert_after_value(self, value, new_value):
       
        current = self.head
        while current is not None:
            if current.data == value:
                #append at the end of the list if the tail is pointing to the value
                if current == self.tail:
                    self.append_at_tail(new_value)
                    return 
                else:
                    #Create a new node 
                    new_node = DoublyLinkedList.Node(new_value)
                    #node containing value 
                    before = new_node.prev   
                    # node after the one containing value 
                    after = new_node.next 
                    #connect before with new node
                    before.next = new_node 
                    #connect after with new node
                    after.prev = new_node 
                # return after insertion 
                return 
            #move to the next node
            current = current.next 

```
### Inserting and removing at the tail of a Doubly Linked List 
----------
```python 
"""Inserting at tail of a Doubly Linked List"""

def append_at_tail(self, value):
        #Create a new node 
        new_node = DoublyLinkedList.Node(value)
        #Check if the list is empty 
        if self.head is None:
            #Point the head and tail to the new node 
            self.head = new_node
            self.tail = new_node
            return 
        else:
            #set the new node on the next available spot 
            self.tail.next = new_node
            #point the new node to the previous node 
            new_node.prev = self.tail
            #point the tail to the new node
            self.tail = new_node
        #Keep track of the length of the list 
        self.length += 1

"""Removing at tail of a Doubly Linked List"""
  def remove_at_tail(self):
        #Check if the list is empty 
        if self.length == 0:
            return None
        #create a variable that keeps track of the current node
        current = self.tail
        #Check if there is only one node in the list
        if self.length  == 1:
                self.head = None
                self.tail = None
        else:
            #point the tail to the previous node  
            self.tail = self.tail.prev
            #set the next of the new tail as None 
            self.tail.next = None
            #set the prevous of the current node to None 
            current.prev = None 
            #Decrease the length 
        self.length -= 1
        return current.value
```
## Problem to solve
------
### Question 
------
Complete the remove node value method and use the below test cases to check if your method is corrent.Provided is the Doubly Linked List class and its Node subclass. **Note** that the remove node value method is inside the Doubly Linked List class. After you can check the [solution](https://github.com/nigel-00/CSE-212-Final-Project/blob/main/linked_list_solution.py) and compare with yours. The [solution](https://github.com/nigel-00/CSE-212-Final-Project/blob/main/linked_list_solution.py) has all the methods inside the Doubly Linked List that where shown as examples in the tutorial.

**NB**- Make sure you complete all the examples methods above because they are all connected.

```python 
class DoublyLinkedList:
    """The Node class is a sub class of the Doubly Linked Class"""
    class Node:
        def __init__(self, value):
            #Node value 
            self.value = value 
            #Next pointer 
            self.next = None
            #Previous pointer
            self.prev = None
    """The constructor of the Doubly Linked List class"""
    def __init__(self, value):
        #Create a new node 
        new_node = DoublyLinkedList.Node(value)
        #Point the head to the new node 
        self.head = new_node 
        #Point the tail to the ne node 
        self.tail = new_node 
        #Initial length of the List
        self.length =  1

    #Make sure you include all the other methods above in order for your remove node value methods to work.

    """Complete the remove node value method"""

    def remove_node_value(self, value):

        #Your code goes here!

Test cases
----------
# Create your Doubly Linked List
my_list = DoublyLinkedList()
#Add some nodes to your list 
my_list.append_at_head(6)
my_list.append_at_tail(7)
my_list.append_at_tail(8)
my_list.append_at_tail(9)
#Go ahead and test our your coded remove node value method 
my_list.remove_node_value(7)
my_list.remove_node_value(6)
my_list.remove_node_value(8)
```




