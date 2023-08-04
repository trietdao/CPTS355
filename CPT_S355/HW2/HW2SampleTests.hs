module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import HW2


p1a_test1 = TestCase (assertEqual "merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2 [2,5,6,8,9] [1,3,4,5,7,8,10]) )
p1a_test2 = TestCase (assertEqual "merge2 [0,0,0,0,4,(-2)] [1,2,3,4,5]" [0,0,0,0,1,2,3,4,4,5,5]  (merge2 [0,0,0,0,4,(5)] [1,2,3,4,5]) )        --student's test case 1 
p1a_test3 = TestCase (assertEqual "merge2 [10,20,30] [-10,40,100]" [-10,10,20,30,40,100]  (merge2 [10,20,30] [-10,40,100]) )                   --student's test case 2
p1b_test1 = TestCase (assertEqual "merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]" [1,2,3,4,5,5,6,7,8,8,9,10]  (merge2Tail [2,5,6,8,9] [1,3,4,5,7,8,10]) )
p1b_test2 = TestCase (assertEqual "merge2 [0,0,0,0,4,(-2)] [1,2,3,4,5]" [0,0,0,0,1,2,3,4,4,5,5]  (merge2 [0,0,0,0,4,(5)] [1,2,3,4,5]) )         --student's test case 1 
p1b_test3 = TestCase (assertEqual "merge2 [10,20,30] [-10,40,100]" [-10,10,20,30,40,100]  (merge2 [10,20,30] [-10,40,100]) )                    --student's test case 2
p1c_test1 = TestCase (assertEqual "mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]" [-3,-2,-1,1,2,3,4,5,8,9]  (mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9]]) )
p1c_test2 = TestCase (assertEqual "mergeN [[(-5), (-3)],[-100, -1000, 30,0],[100, 200, 400,4,-4], [], [-999]]" [-999,-100,-1000,-5,-3,30,0,100,200,400,4,-4]  (mergeN [[(-5), (-3)],[-100, -1000, 30,0],[100, 200, 400,4,-4], [], [-999]] ) )  --student's test case 1
p1c_test3 = TestCase (assertEqual "mergeN [[],[],[]]" [0]  (mergeN [[],[],[],[0]]) )                                        --student's test case 2


p2a_test1 = TestCase (assertEqual "getInRange (-5) 5 [10,5,0,1,2,-5,-10]" [0,1,2]  (getInRange (-5) 5 [10,5,0,1,2,-5,-10]) )
p2a_test2 = TestCase (assertEqual "getInRange (-1) 1 [-2,2,3,4,5]" [] (getInRange (-1) 1 [-2,2,3,4,5]) )
p2a_test3 = TestCase (assertEqual "getInRange (0) 0 [-2,2,0,4,5]" [] (getInRange (0) 0 [-2,2,0,4,5]) )                     --student's test case 1
p2a_test4 = TestCase (assertEqual "getInRange (3) 4 [3,2,4,2,4,10]" [4,4] (getInRange (3) 5 [3,2,4,2,4,10]) )              --student's test case 2
p2b_test1 = TestCase (assertEqual "countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]" 6 (countInRange 3 10 [[1,2,3,4],[5,6,7,8,9],[10,11]]) )
p2b_test2 = TestCase (assertEqual "countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]" 3 (countInRange (-5) 5 [[-10,-5,-4],[0,4,5],[],[10]]) )
p2b_test3 = TestCase (assertEqual "countInRange (-1) 1 [[0,1,2],[0,1,(-1)],[],[1,1,1,1,(-1)]]" 2 (countInRange (-1) 1 [[0,1,2],[0,1,(-1)],[],[1,1,1,1,(-1)]]) )          --student's test case 1  
p2b_test4 = TestCase (assertEqual "countInRange (2) 4 [[1,1,3],[0,2,(-1)],[5,4,6,3],[2,2,2,(-1)]])" 2 (countInRange (2) 4 [[1,1,3],[0,2,(-1)],[5,4,6,3],[2,2,2,(-1)]]) ) --student's test case 2


p3a_test1 = TestCase (assertEqual "addLengths (FOOT 2) (INCH 5)" (INCH 29) (addLengths (FOOT 2) (INCH 5)) )
p3a_test2 = TestCase (assertEqual "addLengths (YARD 3) (INCH (-3)"  (INCH 105) (addLengths (YARD 3) (INCH (-3))))
p3a_test3 = TestCase (assertEqual "addLengths (FOOT 0) (FOOT 0)"  (INCH 0) (addLengths (FOOT 0) (YARD 0)))                    --student's test case 1
p3a_test4 = TestCase (assertEqual "addLengths (FOOT 100) (YARD (-100)"  (INCH (-2400)) (addLengths (FOOT 100) (YARD (-100)))) --student's test case 2
p3b_test1 = TestCase (assertEqual "addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]" (INCH 262) (addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]) )
p3b_test2 = TestCase (assertEqual "addAllLengths [[YARD 2, FOOT 1], [YARD 1, FOOT 2, INCH 10],[YARD 3]]" (INCH 230) (addAllLengths [[FOOT 5, INCH 0, YARD (-4)], [YARD 4, FOOT 2, INCH 10, YARD(-2)],[YARD 3, INCH 100]]))  --student's test case 1
p3b_test3 = TestCase (assertEqual "addAllLengths [[], [INCH 1, INCH 1],[]]" (INCH 2) (addAllLengths [[], [INCH 1, INCH 1],[]]))  --student's test case 2


p4a_test1 = TestCase (assertEqual ("sumTree "++(show t1)) 32 (sumTree t1) )
p4a_test2 = TestCase (assertEqual ("sumTree "++(show treeInt1)) 19 (sumTree treeInt1) )              --student's test case 1
p4a_test3 = TestCase (assertEqual ("sumTree "++(show treeInt2)) 68 (sumTree treeInt2) )              --student's test case 2


t1_output = NODE 32 (NODE 15 (NODE 9 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 17 (LEAF 8) (LEAF 9))
treeInt1_output = NODE 19 (NODE 10 (NODE 8 (LEAF 3) (LEAF 5)) (LEAF 2)) (NODE 9 (NODE 7 (NODE 20 (NODE 10 (LEAF 3) (NODE 7 (LEAF 3) (LEAF 4))) (LEAF 10)) (LEAF (-13))) (LEAF 2))
treeInt2_output = NODE 68 (NODE 36 (NODE 9 (LEAF 4) (LEAF 5)) (NODE 27 (LEAF 6) (NODE 21 (LEAF 10) (LEAF 11)))) (NODE 32 (LEAF 8) (NODE 24 (LEAF 9) (LEAF 15)))
p4b_test1 = TestCase (assertEqual ("createSumTree "++ (show t1)) (t1_output) (createSumTree t1))
p4b_test2 = TestCase (assertEqual ("createSumTree "++ (show treeInt2)) (treeInt2_output) (createSumTree treeInt2))   --student's test case 1
p4b_test3 = TestCase (assertEqual ("createSumTree "++ (show treeInt1)) (treeInt1_output) (createSumTree treeInt1))   --student's test case 2


p5_test1 = TestCase (assertEqual ("foldListTree (+) 0 "++ (show t4)) 36 (foldListTree (+) 0 t4 ) )
p5_test2 = TestCase (assertEqual ("foldListTree (++) \"\" "++ (show t5)) "School-of-Electrical-Engineering-and-Computer-Science-WSU" (foldListTree (++) "" t5) )
p5_test3 = TestCase (assertEqual ("foldListTree (+) 0 "++ (show listTree1)) 70 (foldListTree (+) 0 listTree1) )                --student's test case 1
p5_test4 = TestCase (assertEqual ("foldListTree (+) 0 "++ (show listTree2)) "christmas =.=" (foldListTree (++) [] listTree2) ) --student's test case 2


-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 3 levels.
treeInt1 = NODE (-2)
            (NODE 0 (NODE 0 (LEAF 3) (LEAF 5)) (LEAF 2))
            (NODE 9 (NODE 0 (NODE 3 (NODE 4 (LEAF 3) (NODE 2 (LEAF 3) (LEAF 4))) (LEAF 10)) (LEAF (-13))) (LEAF 2))
treeInt2 = NODE 0 
            (NODE 0 (NODE 0 (LEAF 4) (LEAF 5)) (NODE 0 (LEAF 6) (NODE 0 (LEAF 10) (LEAF 11)))) 
            (NODE 0 (LEAF 8) (NODE 0 (LEAF 9) (LEAF 15)))  
listTree1 =
  ListNODE
    [ ListLEAF [1, 2, 3]
    , ListNODE
        [ ListLEAF [(-3)]
        , ListLEAF [5, 6]
        , ListNODE
            [ ListLEAF [7]
            , ListLEAF [8]
            , ListNODE
                [ ListLEAF [(-9)]
                , ListLEAF []
                ]
            ]
        ]
    , ListLEAF [11, 12, 13, 14]
    ]
listTree2 =
  ListNODE
    [ ListLEAF ["c", "h", "r"]
    , ListNODE
        [ ListLEAF ["i"]
        , ListLEAF ["s", "t"]
        , ListNODE
            [ ListLEAF ["m"]
            , ListLEAF ["a"]
            , ListNODE
                [ ListLEAF [("s")]
                
                ]
            ]
        ]
    , ListLEAF [" ", "=", ".", "="]
    ]
t1 = NODE 1
         (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6))
         (NODE 7 (LEAF 8) (LEAF 9))
t2 = NODE 0
          (NODE 0 (LEAF 4) (NODE 0 (LEAF 8) (LEAF 9)))
          (NODE 0 (NODE 0 (LEAF 10) (NODE 0 (LEAF 12) (LEAF 13))) (LEAF 7))

t3 = NODE 0 (NODE 0 (NODE 0 (LEAF 4) (LEAF 5)) (LEAF 6))
                (NODE 0 (LEAF 8) (LEAF 9))

t4 = ListNODE
 [ ListNODE [ ListLEAF [1,2,3],ListLEAF [4,5],ListNODE([ListLEAF [6], ListLEAF []]) ],
   ListNODE [],
   ListLEAF [7,8],
   ListNODE [ListLEAF [], ListLEAF []] ]

l1 = ListLEAF ["School","-","of","-","Electrical"]
l2 = ListLEAF ["-","Engineering","-"]
l3 = ListLEAF ["and","-","Computer","-"]
l4 = ListLEAF ["Science"]
l5 = ListLEAF ["-WSU"]
n1 = ListNODE [l1,l2]
n2 = ListNODE [n1,l3]
t5 = ListNODE [n2,l4,l5]

tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,
                   TestLabel "Problem 1b - test3 " p1b_test3,
                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3,

                   TestLabel "Problem 2a - test1 " p2a_test1,
                   TestLabel "Problem 2a - test2 " p2a_test2,
                   TestLabel "Problem 2a - test3 " p2a_test3,
                   TestLabel "Problem 2a - test4 " p2a_test4,
                   TestLabel "Problem 2b - test1 " p2b_test1,
                   TestLabel "Problem 2b - test2 " p2b_test2,
                   TestLabel "Problem 2b - test3 " p2b_test3,
                   TestLabel "Problem 2b - test4 " p2b_test4,

                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,
                   TestLabel "Problem 3a - test3 " p3a_test3,
                   TestLabel "Problem 3a - test4 " p3a_test4,
                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,

                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4a - test3 " p4a_test3,

                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 4b - test3 " p4b_test3,

                   TestLabel "Problem 5 - test1 " p5_test1,
                   TestLabel "Problem 5 - test2 " p5_test2,
                   TestLabel "Problem 5 - test3 " p5_test3,
                   TestLabel "Problem 5 - test4 " p5_test4
                 ]


-- shortcut to run the tests
run = runTestTT  tests
