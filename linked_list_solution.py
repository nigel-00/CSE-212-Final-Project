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
    
    def append_at_tail(self, value):
        #Create a new node 
        new_node = DoublyLinkedList.Node(value)
        #Check if the list is empty 
        if self.head is None:
            #Point the head and tail to the new node 
            self.head = new_node
            self.tail = new_node
        else:
            #set the new node on the next available spot 
            self.tail.next = new_node
            #point the new node to the previous node 
            new_node.prev = self.tail
            #point the tail to the new node
            self.tail = new_node
        #Keep track of the length of the list 
        self.length += 1
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

    def print_list(self):
        #Start from the head 
        current = self.head
        #Loop through the linked list 
        while current is not None:
            #Print the value of current everytime you move
            print(current.value)
            #set current to the next node 
            current = current.next

    def remove_node_value(self, value):
            #Check if list is empty
            if self.length == 0:
                return None 
            #set tail to none if there is one item in list
            if self.length == 1:
                self.tail = None 
            #keep track of the current node 
            current  = self.head
            while current is not None:
                #check if the value on current is same as value in search 
                if current.value == value:
                    #check if current is the head 
                    if  current == self.head:
                        self.remove_at_head()
                        break
                    #check if value on current is same as tail 
                    elif current == self.tail:
                        self.remove_at_tail()
                        break
                    else: 
                        #set the node before the node containing value
                        before = current.prev
                        #set the node after the node containing value
                        after = current.next 
                        #connect the node before the node containing value and the node after the node containing value
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        break
                #move to the next node 
                current = current.next 
# Create your Doubly Linked List
my_list = DoublyLinkedList(5)
#Add some nodes to your list 
my_list.append_at_head(6)
my_list.append_at_tail(7)
my_list.append_at_tail(8)
my_list.append_at_tail(9)
#Go ahead and test our your coded remove node value method 
my_list.remove_node_value(7)
my_list.remove_node_value(6)
my_list.remove_node_value(8)
my_list.print_list()