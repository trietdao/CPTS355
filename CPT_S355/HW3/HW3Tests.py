import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.addedSprints = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        # addNLogs input/output
        self.logList = [self.log1,self.log2,self.log3,self.log4]
        self.sprintSummary = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20, 'Kelly': 20}, 'task6': {'Aaron': 8, 'Helen': 26, 'Alex': 15}}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3),('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1),('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1),('some', 1), ('test', 1)]

    #STUDENTS' test inputs/outputs:
        #TEST Q1a (sprintLog):
        self.input1_Q1a= {'John': {'task5': 12},'Sarah': {'task6': 18},'Michael': {'task5': 8},'Emily': {'task6': 14},'David': {'task5': 6},'Sophia': {'task6': 20}}
        self.output1_Q1a = {'task5': {'John': 12, 'Michael': 8, 'David': 6}, 'task6': {'Sarah': 18, 'Emily': 14, 'Sophia': 20}}
        self.input2_Q1a = {'Alice': {'job1': 5, 'job2': 2},'Bob': {'job1': 10},'Charlie': {'job1': 15, 'job2': 2},'Dave': {'job2': 10},'Eve': {'job2': 10},'Frank': {'job3': 16}}
        self.output2_Q1a = {'job1': {'Alice': 5, 'Bob': 10, 'Charlie': 15}, 'job2': {'Alice': 2, 'Charlie': 2, 'Dave': 10, 'Eve': 10}, 'job3': {'Frank': 16}}
        
        #TEST Q1b (addSprints):
        self.input1_Q1b = {'projectX': {'Alice': 5, 'Rae': 10, 'Kelly': 8, 'Bob': 11, 'Eva': 4},'projectY': {'Rae': 4, 'Bob': 2, 'Aaron': 15, 'Charlie': 7},'projectZ': {'Kelly': 5, 'Bob': 1, 'Ethan': 12, 'Helen': 10, 'Frank': 3}}
        self.input2_Q1b = {'projectX': {'Alice': 6, 'Eve': 9, 'John': 7, 'Rae': 10},'projectY': {'Eve': 3, 'John': 5, 'Aaron': 14, 'Michael': 8},'projectZ': {'John': 4, 'Eve': 2, 'Michael': 11, 'Sophia': 6}}
        self.output1_Q1b = {'projectX': {'Alice': 11, 'Rae': 20, 'Kelly': 8, 'Bob': 11, 'Eva': 4, 'Eve': 9, 'John': 7}, 'projectY': {'Rae': 4, 'Bob': 2, 'Aaron': 29, 'Charlie': 7, 'Eve': 3, 'John': 5, 'Michael': 8}, 'projectZ': {'Kelly': 5, 'Bob': 1, 'Ethan': 12, 'Helen': 10, 'Frank': 3, 'John': 4, 'Eve': 2, 'Michael': 11, 'Sophia': 6}} 
        self.input3_Q1b = {'assignment1' : {'Matt': 5, 'IQ' : 5}, 'assignment2' : {'Kelly': 10, 'Matt' : 3}}
        self.input4_Q1b = {'assignment1' : {'John': 20, 'Lame' : 1, 'Matt' : 2}, 'assignment2' : {'Sand': 3, 'Toast' : 8}}
        self.output2_Q1b = {'assignment1': {'Matt': 7, 'IQ': 5, 'John': 20, 'Lame': 1}, 'assignment2': {'Kelly': 10, 'Matt': 3, 'Sand': 3, 'Toast': 8}}
        
        #TEST Q1c (addNLogs):
        self.Q1c_input1 = [self.input1_Q1a, self.input2_Q1a]
        self.Q1c_output1 = {'task5': {'John': 12, 'Michael': 8, 'David': 6}, 'task6': {'Sarah': 18, 'Emily': 14, 'Sophia': 20}, 'job1': {'Alice': 5, 'Bob': 10, 'Charlie': 15}, 'job2': {'Alice': 2, 'Charlie': 2, 'Dave': 10, 'Eve': 10}, 'job3': {'Frank': 16}}
        self.Q1c_input2 = [{'some' : {'thing' : 0}}]
        self.Q1c_output2 = {'thing': {'some': 0}}
        
        #TEST Q2a (lookupVal):
        self.Q2a_input1 = []
        self.Q2a_ouput1 = None
        self.Q2a_input2 = [{},{},{}]
        self.Q2a_ouput2 = None 
        self.Q2a_input3 = [{"a": 10, "b": True, "c": "apple"},{"a": 20, "b": False},{"b": False, "c": "orange", "d": 5},{"a": 30, "c": "banana", "d": 8, "e": True}]
        self.Q2a_ouput3 = 30
        
        #TEST Q2b (lookupVal2):
        self.Q2b_input1 = [(0, {"x": 0, "y": True, "z": "zero"}),(0, {"x": 1, "y": "one"}),(1, {"y": False, "z": "two"}),(2, {"x": 3, "z": "three", "w": 4}),(3, {"v": "five"})]
        self.Q2b_output1 = False
        
        #TEST Q3 (unzip):
        self.Q3_input1 = [(1, "apple", {1: "apple"}),(2, "banana", {2: "banana"}),(3, "cherry", {3: "cherry"}),(4, "date", {4: "date"})]
        self.Q3_output1 = ([1, 2, 3, 4], ['apple', 'banana', 'cherry', 'date'], [{1: 'apple'}, {2: 'banana'}, {3: 'cherry'}, {4: 'date'}])
        self.Q3_input2 = [(None, None, None)]
        self.Q3_output2 = ([None], [None], [None])
        
        #TEST Q5:
        self.Q5_input = ["The", "sun", "dipped", "below", "the", "horizon.", "like", "tiny", "pinpricks.", "Please", "note", "that", "this", "paragraph", "was", "generated."]
        self.histogram_output1 = [('CptS', 3), ('355', 3), ('Assignment', 3), ('3', 3), ('-', 5), ('Python', 3), ('Warmup', 3), ('This', 1), ('is', 1), ('a', 1), ('text', 2), ('test', 1), ('file', 1), ('for', 2), ('With', 1), ('some', 1), ('repeated', 1), ('.', 1)]
        self.histogram_output2 = [('The', 1), ('sun', 1), ('dipped', 1), ('below', 1), ('the', 1), ('horizon.', 1), ('like', 1), ('tiny', 1), ('pinpricks.', 1), ('Please', 1), ('note', 1), ('that', 1), ('this', 1), ('paragraph', 1), ('was', 1), ('generated.', 1)]
    
    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)
        self.assertDictEqual(sprintLog(self.input1_Q1a),self.output1_Q1a)     #student's test case 1 
        self.assertDictEqual(sprintLog(self.input2_Q1a ),self.output2_Q1a)     #student's test case 2
    
    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints)
        self.assertDictEqual(addSprints(self.input1_Q1b,self.input2_Q1b),self.output1_Q1b)  #student's test case 1 
        self.assertDictEqual(addSprints(self.input3_Q1b,self.input4_Q1b),self.output2_Q1b)  #student's test case 2 
        
    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList),self.sprintSummary)
        self.assertDictEqual(addNLogs(self.Q1c_input1),self.Q1c_output1)        #student's test case 1
        self.assertDictEqual(addNLogs(self.Q1c_input2),self.Q1c_output2)        #student's test case 2

    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)
        self.assertEqual(lookupVal(self.Q2a_input1,"er"),self.Q2a_ouput1)        #student's test case 1
        self.assertEqual(lookupVal(self.Q2a_input2,"2"),self.Q2a_ouput2)         #student's test case 2
        self.assertEqual(lookupVal(self.Q2a_input3,"a"),self.Q2a_ouput3)         #student's test case 3

    def test_lookupVal2(self):
        self.assertEqual(lookupVal2(self.Q2b_input1,"y"),self.Q2b_output1)       #student's test case 1
        self.assertEqual(lookupVal2(self.Q2b_input1,"z"),"three")                #student's test case 2
        self.assertEqual(lookupVal2(self.Q2b_input1,"0"),None)                   #student's test case 3
        self.assertEqual(lookupVal2(self.Q2b_input1,"w"),4)                      #student's test case 4
    
    def test_unzip(self):
        self.assertEqual(unzip (self.Q3_input1),self.Q3_output1)                     #student's test case 1
        self.assertEqual(unzip ([(None, None, None)]),([None], [None], [None]))      #student's test case 2

    def test_numPaths(self):
        self.assertEqual(numPaths(15,3,[(2,1),(10,2)]), 9)              #student's test case 1
        self.assertEqual(numPaths(10,9,[(2,1),(10,8)]), 6435)           #student's test case 2

    def test_iterFile(self):
        mywords = iterFile("HW3testfile.txt")
        self.assertEqual(mywords.__next__(),"CptS")
        self.assertEqual(mywords.__next__(),"355")
        self.assertEqual(mywords.__next__(),"Assignment")
        restofFile = []
        for word in mywords:
            restofFile.append(word)
        self.assertEqual(restofFile,self.filetokens[3:])
        
        mywords2 = iterFile ("TestFile1.txt")           #student's test case 1
        self.assertEqual(mywords2.__next__(),"The")
        self.assertEqual(mywords2.__next__(),"sun")
        self.assertEqual(mywords2.__next__(),"dipped")
        self.assertEqual(mywords2.__next__(),"below")
        self.assertEqual(mywords2.__next__(),"the")
        restofFile1 = []
        for word in mywords2:
            restofFile1.append(word)
        self.assertEqual(restofFile1,self.Q5_input[5:])
        
        mywords2 = iterFile ("TestFile2.txt")           #student's test case 2
        self.assertEqual(mywords2.__next__(),"The")
        self.assertEqual(mywords2.__next__(),"sun")
        self.assertEqual(mywords2.__next__(),"dipped")
        self.assertEqual(mywords2.__next__(),"below")
        self.assertEqual(mywords2.__next__(),"the")
        restofFile2 = []
        for word in mywords2:
            restofFile2.append(word)
        self.assertEqual(restofFile2,self.Q5_input[5:])
        
    def test_wordHistogram(self):
        self.assertEqual(wordHistogram(iterFile("HW3testfile.txt")),self.histogram_output1)     #student's test case 1
        self.assertEqual(wordHistogram(iterFile("TestFile2.txt")),self.histogram_output2)       #student's test case 2
        

if __name__ == '__main__':
    unittest.main()

