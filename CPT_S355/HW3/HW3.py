# Name: Dao Minh Triet 
# ID: 011753385
# CPT_S 355
#Assignment 3

from functools import reduce
#1a
def sprintLog (dict):
    temp = {}
    for key, value in dict.items():
        for task, hour in value.items():
            if task in temp:
                temp[task][key] = hour
            else:
                temp[task] = {key:hour}             
    return temp
#1a

#1b
def addSprints(sprint1, sprint2):
    temp = {}
    for key, value in sprint1.items():
        temp[key] = value
    for task, nestedDict in sprint2.items():
        if task in temp:
            for name, hour in nestedDict.items():
                if name in temp[task]:
                    temp[task][name] += hour
                else:
                    temp[task][name] = hour
        else:
            temp[task] = nestedDict       
    return temp 
#1b
#2a
def lookupVal(L,k):
    j = 0
    for i in range (len(L)):
        if k in L[len(L)- i - 1]:
            return L[len(L)- i - 1][k]       
#2a
#1c
def addNLogs(logList):
    return reduce(addSprints, map(sprintLog, logList))
#1c

#2a
def lookupVal(L,k):
    j = 0
    for i in range (len(L)):
        if k in L[len(L)- i - 1]:
            return L[len(L)- i - 1][k]       
#2a

#2b
def lookupVal2(tL,k):
    index_list = len(tL)-1
    def helper (indexOfList, nestedList, k):
        if (indexOfList == 0):                            # base case 1: when reaching the end of the list. 
            checkItem = lookupVal([nestedList[0][1]],k)   # nestedList[0][1] : dictionary in the first tuple in the big List. 
            return checkItem    
        else:
            checkItem = lookupVal([nestedList[indexOfList][1]],k)
            if (checkItem == None):
                return helper(nestedList[indexOfList][0], tL, k)   
            else:
                return (checkItem)
    return (helper(index_list,tL,k))                      
#2b

#3
def unzip(L):
    return tuple(reduce(lambda acc, value:(acc[0] + [value[0]], acc[1] + [value[1]], acc[2]+ [value[2]]), L , ([],[],[])))
#3

#4
def numPaths(m,n,blocks):   
    if (m,n) in blocks or m < 1 or n < 1:
        return 0
    if m == 1 and n == 1:
        return 1      
    else: 
        return numPaths(m-1,n, blocks) + numPaths(m,n-1,blocks)
        
#4

#5a
class iterFile():
    def __init__(self,file):
        self.file = open(file)
        self.line = []
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):   
        try:        
            if self.index == len(self.line):
                self.line = self.file.readline().split()     
                return self.line[0]
            elif self.index == len(self.line) - 1:   
                self.index = 0 
                self.line = self.file.readline().split()
                if self.line != []:
                    return self.line[0]
                else:
                    self.line = self.file.readline().split()
                    return self.line[0]
            else: 
                self.index += 1
                return self.line[self.index]     
        except:                                     #stop iteration when file has been read completely
            raise StopIteration
#5a          

#5b
def wordHistogram(words):
    histogram = {}
    for word in words:
        if word not in histogram:
            histogram[word] = 1
        else: 
            histogram[word] += 1
    return(list(histogram.items()))
#5b


    
#5
# class iterFile():
#     def __init__(self, file):
#         self.file = open(file)
#         self.line = []
#     def __iter__(self):
#         return self 
#     def __next__(self):     
#         try: 
#             if len(self.line) == 0: 
#                 self.line = self.file.readline().split()              
#                 word = self.line.pop(0)
#                 return word
#             else: 
#                 word = self.line.pop(0)
#                 return word   
#         except:                     #stop iteration when file has been read completely
#             raise StopIteration  