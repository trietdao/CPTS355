import sys
import io
import unittest
from HW4_skeleton import *

class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1],"(Hello)")
        
        opstack.clear()                                 
        opPush("(Hello)")
        opPush(1)
        opPush(2)
        self.assertEqual(opstack,['(Hello)',1,2])       #student's test case 1 --opPush--
        
        opstack.clear()                                 
        opPush(1)
        opPush(0)
        self.assertEqual(opstack,[1,0])                 #student's test case 2 --opPush--   
    
    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)

    def testOpPop(self):                            
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)                     
        
        opstack.clear()
        opPush("(Hello)")
        opPush(10)
        self.assertEqual(opPop(),10)                    #student's test case 1 --opPop--             
        
        opstack.clear()
        opPush(0)
        opPush("(Hello)")
        opPush(100)
        self.assertEqual(opPop(),100)                   #student's test case 2 --opPop--
    
    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})
        
        dictstack.clear()
        dictPush({"/y":3})
        self.assertEqual(dictstack[-1],{"/y":3})                      #student's test case 1 --DictPush--
        
        dictstack.clear()
        dictPush({"/y":3} )
        dictPush({"/x":5} )
        self.assertEqual(dictstack,[{"/y":3}, {"/x":5}])              #student's test case 2 --DictPush--

    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)
        
        dictstack.clear()
        dictPush({})
        dictPush({"/y":3})
        dictPush({"/x":5})
        dictPop()
        self.assertEqual(len(dictstack),2)                          #student's test case 1 --dictPop--
        
        dictstack.clear()
        dictPush({})
        dictPush({"/x":5})
        dictPop()
        self.assertEqual(dictstack,[{}])                            #student's test case 2 --dictPop--

    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)
        
        dictstack.clear()
        define("/a",1)
        define("/b",3)
        self.assertEqual(len(dictstack),2)                         #student's test case 1 --Define--


        dictstack.clear()
        define("/a",1)
        define("/b",3)
        self.assertEqual(dictstack[1],{'/b': 3})                   #student's test case 2 --Define--


    def testLookup(self):
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        self.assertEqual(lookup("n1"),"(hornswaggle)")
        
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        opPush("/n2")       
        opPush("(bee)")  
        psDef()
        self.assertEqual(lookup("n2"),"(bee)")                     #student's test case 1 --LookUp--
        
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        opPush("/n2")       
        opPush("(bee)")  
        psDef()
        opPush("/n3")       
        opPush(3)  
        psDef()
        self.assertEqual(lookup("n3"),3)                          #student's test case 2 --LookUp--

    def testAdd(self):
        opstack.clear()     
        opPush(1)       
        opPush(2)       
        add()       
        self.assertEqual(opPop(),3)                 
        
        opstack.clear()     
        opPush(0)       
        opPush(0)       
        add()       
        self.assertEqual(opPop(),0)                                #student's test case 1 --Add1--
        
        opstack.clear()     
        opPush(1)       
        opPush((-2))       
        add()               
        self.assertEqual(opPop(),-1)                              #student's test case 2 --Add1--

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()       
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        add()       
        self.assertEqual(opPop(),"(string1)")
        self.assertEqual(opPop(),"(string)")                      #student's test case 1 --Add2--
        
        opstack.clear()     
        opPush(0)
        opPush({'x':1})
        add()       
        self.assertEqual(opPop(),{'x':1})
        self.assertEqual(opPop(),0)                               #student's test case 2 --Add2--

    def testSub(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        sub()       
        self.assertEqual(opPop(),"(string1)")
        self.assertEqual(opPop(),"(string)")                      #student's test case 1 --sub--
        
        opstack.clear()     
        opPush(0)
        opPush({'x':1})
        sub()       
        self.assertEqual(opPop(),{'x':1})
        self.assertEqual(opPop(),0)                               #student's test case 1 --sub--
    
    def testMul(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        mul()       
        self.assertEqual(opPop(),"(string1)")
        self.assertEqual(opPop(),"(string)")                      #student's test case 1 --mul--
        
        opstack.clear()     
        opPush(0)
        opPush({'x':1})
        mul()       
        self.assertEqual(opPop(),{'x':1})
        self.assertEqual(opPop(),0)                               #student's test case 2 --mul--

    def testDiv(self):
        opstack.clear()
        opPush(4)
        opPush(2)
        div()
        self.assertEqual(opPop(),2)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        div()       
        self.assertEqual(opPop(),"(string1)")
        self.assertEqual(opPop(),"(string)")                      #student's test case 1 --div--
        
        opstack.clear()     
        opPush(0)
        opPush({'x':1})
        div()       
        self.assertEqual(opPop(),{'x':1})
        self.assertEqual(opPop(),0)                               #student's test case 2 --div--
    
    def testMod(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        mod()       
        self.assertEqual(opPop(),"(string1)")
        self.assertEqual(opPop(),"(string)")                      #student's test case 1 --mod--
        
        opstack.clear()     
        opPush(0)
        opPush({'x':1})
        mod()       
        self.assertEqual(opPop(),{'x':1})
        self.assertEqual(opPop(),0)                               #student's test case 2 --mod--

    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)
        
        opstack.clear()     
        opPush("(string)")
        opPush("(string1)")
        eq()       
        self.assertEqual(opPop(),False)                        #student's test case 1 --eq--
        
        opstack.clear()     
        opPush("(hi)")
        opPush(3)
        eq()       
        self.assertEqual(opPop(),3)                            #student's test case 2 --eq--

    def testLt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)      
        
        opstack.clear()
        opPush(5)
        opPush(3)
        lt()
        self.assertEqual(opPop(),False)                        #student's test case 1 --Lt--
        
        opstack.clear()
        opPush("(hi)")
        opPush(3)
        lt()
        self.assertEqual(opPop(),3)                            #student's test case 2 --Lt--

    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)
        
        opstack.clear()
        opPush(9)
        opPush(3)
        gt()
        self.assertEqual(opPop(),True)                          #student's test case 1 --Gt--
        
        opstack.clear()
        opPush("(hi)")
        opPush(3)
        gt()
        self.assertEqual(opPop(),3)                             #student's test case 2 --Gt--
        
        opstack.clear()
        opPush(3)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)                         #student's test case 3 --Gt--

    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)
        
        opstack.clear()
        opPush('()')
        length()
        self.assertEqual(opPop(),0)                             #student's test case 1 --Length--
        
        opstack.clear()
        opPush(1)
        length()
        self.assertEqual(opPop(),1)                             #student's test case 2 --Length--

    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))
        
        opstack.clear()
        opPush("()")
        opPush(0)
        get()
        self.assertEqual(opPop(),0)                             #student's test case 1 --Get--
        
        opstack.clear()
        opPush("(CptS355)")
        opPush(3)
        get()
        self.assertEqual(opPop(),ord('S'))                      #student's test case 2 --Get--

    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")
        
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(0)
        getinterval()
        self.assertEqual(opPop(),"()")                          #student's test case 1 --getinterval--
        
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(-1)
        getinterval()
        self.assertEqual(opPop(), -1)                          #student's test case 2 --getinterval--

        opstack.clear()
        opPush("(CptS355)")
        opPush(3)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(S35)") 
        
    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")
        
        opstack.clear()
        opPush("(CptS355)")
        opPush("(CptS355)")
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")
        self.assertEqual(opPop(),"(CptS355)")
        self.assertEqual(opPop(),"(CptS355)")                   #student's test case 1 --put--
         
        clear()
        opPush("(This is a test _)") 
        opPush("(This is a test _)") 
        opPush("(This is a test _)") 
        dup() 
        opPush("/s") 
        exch() 
        psDef() 
        dup() 
        opPush(15) 
        opPush(48) 
        put() 
        self.assertEqual(opPop(),"(This is a test 0)")         
        self.assertEqual(opPop(),"(This is a test _)")          #student's test case 2 --put--
        self.assertEqual(opPop(),"(This is a test _)")

    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)
        
        opstack.clear()
        opPush(3)
        opPush(3)
        dup()
        self.assertEqual(len(opstack),3)                        #student's test case 1 --dup--
        
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(opPop(),3)                             #student's test case 2 --dup--

    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)
        
        opstack.clear()
        opPush(1)
        opPush("(HI)")
        opPush("(2)")
        opPush(4)
        pop()
        self.assertEqual(len(opstack), 3)                       #student's test case 1 --Pop--
        
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(5)
        pop()
        self.assertEqual(len(opstack),3)                        #student's test case 2 --Pop--
    
    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)
        
        opstack.clear()
        opPush(1)
        opPush("(HI)")
        opPush("(2)")
        opPush(4)
        clear()
        self.assertEqual(len(opstack),0)                        #student's test case 1 --clear--
        
        opstack.clear()
        clear()
        self.assertEqual(len(opstack),0)                        #student's test case 2 --clear--

    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])
        
        opstack.clear()
        opPush("(Hi)")
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,"(Hi)"])                #student's test case 1 --exch--
        
        opstack.clear()
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2])                       #student's test case 2 --exch--

    def testRoll(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,4,3])
        
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(5)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,3,4,5,3])     #student's test case 1  --roll--
        
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(5)
        opPush(5)
        opPush(-2)
        roll()
        self.assertListEqual(opstack,[3,4,5,1,2])       #student's test case 2  --roll--
    
    def testStack(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")

        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "")
        
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")
        
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(("(Hi)"))
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "(Hi)\n2\n")             #student's test case 1  --stack--
        
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(None)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "None\n2\n")             #student's test case 2  --stack--
                
    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)            
    
        opstack.clear()
        opPush(2)
        opPush(3)
        opPush(4)
        psDict()
        self.assertEqual(len(opstack), 3)                            #student's test case 1  --psDict-- 
        
    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})
        
        opstack.clear()
        dictstack.clear()
        opPush("/x")
        opPush(2)
        psDef()
        opPush(lookup("x"))
        self.assertEqual(opPop(),2)                                   #student's test case 1  --psDef-- 
        
        opstack.clear()
        dictstack.clear()
        opPush("/zz")
        opPush(100)
        psDef()
        opPush(lookup("zz"))
        self.assertEqual(opPop(),100)                                 #student's test case 2  --psDef-- 
    

if __name__ == '__main__':
    unittest.main()

