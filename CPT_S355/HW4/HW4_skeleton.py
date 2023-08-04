#Name: Dao Minh Triet 
#ID: 011753385
#Assignment 4 -- CptS355

#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations


opstack = []  #assuming top of the stack is the end of the list

def is_string(string):
    if (type(string) is str):
        if (string[0] == '(' and string[-1] == ')'):
            return True
        else:
            return False 
def is_number(value):
    return isinstance(value, (int, float))
def is_name_constant(name):
    if (type(name) is str):
        if (name[0] == '/'):
            return True
        else:
            return False
def is_dict(name):
    if (type(name) is dict):
        return True
    else:
        return False
# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    if len(opstack) > 0:
        value = opstack[len(opstack) -1]
        opstack.pop(len(opstack)-1)
        return value
    else:
        print("Not enough element in --opPop--") 
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.
def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name
def dictPop():
    if len(dictstack) > 0:
        dictstack.pop(len(dictstack) - 1)
    else:
        print("Error message")
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    if type(d) is dict:
        dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if is_name_constant(name) == True:
        dictstack.append({name:value})
    else:
        print("undefined in " + name)
    #add name:value pair to the top dictionary in the dictionary stack.
    #Keep the '/' in the name constant.
    #Your psDef function should pop the name and value from operand stack and
    #call the “define” function.

def lookup(name):
    for item in dictstack:
        a = '/'
        if list(item.keys()) == [a + name]:
            return item[a + name]
    print ("Undefined in " + a + name)
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if (is_number(first) and is_number(second)):
            result = first + second 
            opPush(result)
        else:
            opPush(second)
            opPush(first)
    else:
        print("Need at least 2 parameters")
def sub():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if (is_number(first) and is_number(second)):
            result = second - first
            opPush(result)
        else:
            opPush(second)
            opPush(first)
    else:
        print("Need at least 2 parameters")
def mul():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if (is_number(first) and is_number(second)):
            result = first * second 
            opPush(result)
        else:
            opPush(second)
            opPush(first)
    else:
        print("Need at least 2 parameters")

def div():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if (is_number(first) and is_number(second)):
            result = second / first
            opPush(result)
        else:
            opPush(second)
            opPush(first)
    else:
        print("Need at least 2 parameters")

def mod():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if (is_number(first) and is_number(second)):
            result = second % first
            opPush(result)
        else:
            opPush(second)
            opPush(first)
    else:
        print("Need at least 2 parameters")

def eq():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if type(first) != type(second):
            opPush(second)
            opPush(first)
            print("Wrong type in --eq()--")
        elif (first == second):          
            opPush(True)
        else:
            opPush(False)
    else:
        print("Need at least 2 parameters")
def lt():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if type(first) != type(second):
            opPush(second)
            opPush(first)
            print("Wrong type in --lt()--")
        elif (second < first):          
            opPush(True)
        else:
            opPush(False)
    else:
        print("Need at least 2 parameters")

def gt():
    if (len(opstack) > 1):
        first =  opPop() 
        second = opPop()
        if type(first) != type(second):
            opPush(second)
            opPush(first)
            print("Wrong type in --lt()--")
        elif (second > first):          
            opPush(True)
        else:
            opPush(False)
    else:
        print("Need at least 2 parameters")

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put

def length():
    if (len(opstack) > 0):     
        string = opPop()
        if type(string) != str:
            opPush(string)
        elif (is_string(string)):      
            result = len(string) -2 
            opPush(result) 
        else:
            opPush(string)
            print("Wrong input's type")
    else:
        print("Not enough element")
    
def get():
    if (len(opstack) > 1):
        index = opPop()
        string = opPop()
        if is_string(string) and is_number(index):
            if (0 <= index < len(string)-2):    #index is good 
                result = ord(string[index + 1])
                opPush(result)
            elif index >= len(string)-2:        #index > string's length
                opPush(string)
                opPush(index)
                print("Range check in --",index, "--")
            else:                               # index < 0 
                opPush(string)
                opPush(index)
                print("Range check in --get--")       
        elif is_name_constant(string):
            opPush(string)
            opPush(index)
            print("Type check in --get--")
        else:
            print("Your input is wrong")
    else:
        print("Not enough element")
        
def getinterval():
    count = opPop()
    startIndex = opPop()
    string = opPop()
    if not(is_number(count) and is_number(startIndex) and type(string) == str and count  >= 0 and count+startIndex <=len(string)):
        opPush(string)
        opPush(startIndex)
        opPush(count)
        print("Input is incorrect in --getinterval--")
    elif count != 0:
        result = string[startIndex + 1]
        for i in range(count - 1):
            result = result + string[startIndex + i + 2]           #get targeted part 
        opPush('(' + result + ')')
        return '(' + result + ')'
    else:                                                           #special case for count = 0
        opPush('()')
        return '()'
    
def put():
    if len(opstack) > 0:
        char = opPop()
        index = opPop()
        string = opPop()
        if type(string) == str and type(index) == int and type(char) == int:
            for i in range (1,len(opstack)+1):                                      #iterate opstack from the end to the beginning 
                if opstack[-i] is string:
                    opstack[-i] = string[:index+1] + chr(char) + string[index+2:]   #modify targeted string               
        else:
            opPush(string)  
            opPush(index)
            opPush(char)
        
#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    if (len(opstack) > 0):
        x = opPop()
        if type(x) != str:
            opPush(x)
            opPush(x)
        else:
            a = x
            new_a = "{}{}".format(a,"")
            opPush(new_a)
            opPush(new_a)       
    else:
        print("Not enough element")
        
def copy():
    j = opPop()
    temp = []
    if j <= len(opstack):
        for i in range (0,j):
            items = opstack[len(opstack) - 1 - i] 
            temp.append(items)
        for items in reversed(temp):
            opPush(items)
    else:
        opPush(j)
        print("stack underflow in --copy--")
        
def pop(): 
    opPop()  
    
def clear():
    opstack.clear()

def exch():
    if len(opstack) >= 2:
        first = opPop()
        second = opPop()
        opPush(first)
        opPush(second)
    else:
        print("stack underflow in --exch--")
        
def roll():
    i = opPop()
    n = opPop()
    if len(opstack) > 0 and len(opstack) >= n >= 0: 
        tail = opstack[len(opstack) -n:]                        #call the targeted part tail
        opstack[len(opstack) -n:] =[]                           #cut the tail part and modify that part only
       
        temp = [None] * len(tail)                               
        for j in range (len(temp)):
            real_index = ((len(temp)- j -1) + i ) % len(temp)  #find the new index after ith rolling 
            temp[real_index] = tail[len(tail) -1 -j]           #put elements in the new position 
        result = temp
        for items in result:
            opstack.append(items)                              #append that new tail into our real stack
    else:
        opPush(n)
        opPush(i)
        print("--not enough element in the stack--")
        
def stack():
    for i in range (1,len(opstack)+1):
        print(opstack[-i])
#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    if (len(opstack) > 0):
        initial_size = opPop()
        opPush({})
    else:
        print("Not enough element in --dict--")
def begin():
    dictionary = opPop()
    if (type(dictionary) is dict):
        dictPush(dictionary)
    else:
        print("Input needs to be a dictionary")

def end():
    dictPop()
    
def psDef():
    if (len(opstack) > 1):
        value = opPop()
        name = opPop()
        define(name,value)   
    else:
        print("Not enough element in --def--")
def main():
    opPush("/n1")
    opPush(3)
    psDef()
    value = lookup("n1")
    print(value)
main() 

        