import sys
import io
import unittest
from HW5_skeleton import *

class HW5Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test1_parse(self):
        input1 = """
        /square {
               dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """
        result = ['/square', ['dup', 'mul'], 'def', '(square)', 4, 'square', 'dup', 16, 
'eq', ['(pass)'], ['(fail)'], 'ifelse', 'stack'] 
        self.assertEqual(parse(tokenize(input1)),result)
    
    def test2_parse(self):
        input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        end
    } def
    n fact stack
    """
        result = ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', [0, 'dict', 
'begin', '/n', 'exch', 'def', 'n', 2, 'lt', [1], ['n', 1, 'sub', 'fact', 
'n', 'mul'], 'ifelse', 'end'], 'def', 'n', 'fact', 'stack']
        self.assertEqual(parse(tokenize(input2)),result)
        
        
    def test3_parse(self):
        input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """
        result = ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, 
['mul'], 'for', 'end'], 'def', 6, 'fact', 'stack'] 
        self.assertEqual(parse(tokenize(input3)),result)
        
        
    def test4_parse(self):
        input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
    """
        result = ['/lt6', [6, 'lt'], 'def', 1, 2, 3, 4, 5, 6, 4, -3, 'roll', 'dup', 'dup', 
'lt6', ['mul', 'mul', 'mul'], 'if', 'stack', 'clear'] 
        self.assertEqual(parse(tokenize(input4)),result)
        
    def test5_parse(self):
        input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
         stack
        """
        result = ['(CptS355_HW5)', 4, 3, 'getinterval', '(355)', 'eq', 
['(You_are_in_CptS355)'], 'if', 'stack']
        self.assertEqual(parse(tokenize(input5)),result)

 
        
    def test1_interpreter(self):
        clear()
        input1 = """
        /square {
               dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """
        result = ['(square)', 16,'(pass)' ]
        interpreter(input1)
        self.assertEqual(opstack,result)
        
    def test2_interpreter(self):
        clear()
        input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
           /n exch def
           n 2 lt
           { 1}
           {n 1 sub fact n mul }
           ifelse
        end
    } def
    n fact stack
    """
        result = ['(facto)',120]
        interpreter(input2)
        self.assertEqual(opstack,result)
        
    def test3_interpreter(self):
        clear()
        input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """
        result = [720]
        interpreter(input3)
        self.assertEqual(opstack,result)
        
    def test4_interpreter(self):
        clear()
        input4 = """
        /lt6 { 6 lt } def  
        1 2 3 4 5 6 4 -3 roll     
        dup dup lt6 {mul mul mul} if 
        stack  
    """
        result = [1,2,6,300]
        interpreter(input4)
        self.assertEqual(opstack,result)
        
    def test5_interpreter(self):
        clear()
        input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
        stack
        """
        result = ['(You_are_in_CptS355)' ]
        interpreter(input5)
        self.assertEqual(opstack,result)    
   
    def test6_interpreter(self):
        input6 = """
        /pow2 {/n exch def
               (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
              } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """
        result = ['/pow2', ['/n', 'exch', 'def', '(pow2_of_n_is)', 'dup', 8, 'n', 48, 
'add', 'put', 1, 'n', -1, 1, ['pop', 2, 'mul'], 'for'], 'def', 
'(Calculating_pow2_of_9)', 'dup', 20, 'get', 48, 'sub', 'pow2', 'stack']  
        self.assertEqual(parse(tokenize(input6)),result)

if __name__ == '__main__':
    unittest.main()

