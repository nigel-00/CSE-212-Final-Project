# Stacks 
## Defination 
------
* A stack is a data structure that stores data, similar to a stack of plates in a kitchen, or a stack of pancakes.
* Astack is a **last in, first out  (LIFO )** data structure.
* The last plate that was added to the stack will be the first to be picked up from the stack.
The element which is added last is picked up first. 
* There are two primary operations performed on stacks **the push and pop** operations.
* The push operation adds an item on top of the list and the pop operations removes the top item on the list.
*  **NB** - the last item to be added is the first item to be removed.
![Stack](https://media.geeksforgeeks.org/wp-content/uploads/20210716162942/stack-660x345.png)

## Stack Implementation 
* There are many ways to implement a stack. I am going to use classes to implement them.
----
### Stack Constructor
---
* **NB** The Node class is part of the Stack class 
```python 
class Stack: 
    class Node:
        def __init__(self, value):
            #A value to be added to a stack 
            self.value = value
            #set next to none 
            self.next = None     
    #constructor for the stack class
    def __init__(self):
        #Top of stack pointing to the new node
        # We dont have to keep track of the bottom because we are only removing from the top 
        self.top = None 
        #height of the stack
        self.height = 0
    #Method to print the stack     
    def print_stack(self):
        #start at the top
        current = self.top 
        #Loop through the stack 
        while current is not None:
            print(current.value)
            #move to the next node 
            current = current.next 

```
### Push method to add items to the stacks 
* Remember that we are adding to the top of the stack (LIFO)
---
```python 
def push(self, value):
        #Create a new node with the value 
        new_node = Stack.Node(value)
        #check if stack is empty
        if self.height == 0:
            #add new node to the top of the stack
            self.top = new_node
        else:
            #next of the new node is the top of the stack 
            new_node.next = self.top 
            #point the top to the new node
            self.top = new_node 
        #Increment height
        self.height += 1
```
### Poping method to remove items from the stack 
* Remember that we are removing from the top of the stack (LIFO)
```python 
def pop(self):
        #check if stack is empty 
        if self.height == 0:
            return None 
        else:
            current = self.top 
            #point the top to the next of the current node 
            self.top = self.top.next
            #remove from stack 
            current.next = None 
            self.height -= 1
            return current.value
```
## Big O Notation
------
| Stack Operation| Description                                   | Peformance     |
| :---:          |     :----:                                    |         :---:  |
| push(value )   | Adds value to the back of the stack           | O(1)           |
| pop (value)    | Removes and returns item at the back of stack | O(1)           |
| empty()        |Returns true if the length of the stack is zero| O(1)           |
| size()         |  Return the size of the stack                 | O(1)           |
---
## Problem to solve 
### Finish implementing the balanced_parentheses method
* The method takes a text with different types of parentheses(symbols)
* These symbols come in pairs so you have to check if the symbols are balanced or not. For example if the **text** = ("{()}") then it is balanced becuase both symbols have open and close parentheses. The same is the case with when the **text** = ("{()"), the "{" doesnt have its close symbol then the text is not balanced
* **Hint** You can create a dictionary that keeps track of the opening symbols. 
* **NB** - dictionaries have key, value pairs and the keys are iterated using a for loop.
* After you finish implenting the method, you can compare with the [solution](https://github.com/nigel-00/CSE-212-Final-Project/blob/main/stacks_solution.py)

#### Here is the starting code for the balanced_parentheses method
```python 
def balanced_parentheses(text):
    
    #your code goes here 

#Test cases 
print(balanced_parentheses("({{}})")) #True
print(balanced_parentheses("({}})"))  #False 
print(balanced_parentheses("([{{}})")) #False 
print(balanced_parentheses("([])")) #True

```

---
