def balanced_parentheses(text):
    #dictionary containing open and closing symbols
    symbols_pairings = {
    '(': ')',
    '{': '}',
    '[': ']'
}  
    #Initialize the instance of a stack 
    stack = Stack()
    #Iterate through the text 
    for char in text:
        #push the char if is the open sysmbols in the dictionary and continue 
        #remember iteration in a dictionary returns the keys not values 
        if char in symbols_pairings:
            stack.push(char)
            continue
        #return false if there is an index error 
        try:
            expected_opening_symbol = stack.pop()
        except IndexError:  
            return False
        #return false if the character is not equal to the value in the dictionary 
        if char != symbols_pairings[expected_opening_symbol]: 
            return False
    #return false if stack has too many opening symbols
    return stack.height == 0 

"""Test cases"""        
print(balanced_parentheses("({{}})")) #True 
print(balanced_parentheses("({}})"))  #False 
print(balanced_parentheses("([{{}})")) #False 
print(balanced_parentheses("([])")) #True 