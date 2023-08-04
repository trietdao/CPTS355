-- CptS 355 - Summer 2023 Assignment 1
-- Name: Dao Minh Triet 
-- ID: 011753385
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}

module HW1
     where

import Data.Char (toUpper)
import Distribution.Simple.Setup (falseArg)

-- 1. exists
exists :: Eq t => t -> [t] -> Bool
exists _ [] = False
exists x (y:ys) = x == y || exists x ys 
--1b. 
--Eq t is a class constrain that indicates type t should be in typeclass Eq t in which type t can perform "==" and "\=" features. 
--So without Eq t in the type signature, the comparison "x==y" can't be executed. 

-- 2. listUnion
listUnion :: Eq a => [a] -> [a] -> [a]
listUnion a b = removeDupl (removeDupl a ++ removeDupl b) 
              where removeDupl :: Eq a => [a] -> [a]
                    removeDupl [] = []
                    removeDupl (x:xs) = x : removeDupl (removeAll x xs)
                         where removeAll :: Eq a => a -> [a] -> [a]
                               removeAll _ [] = []
                               removeAll y (z:zs)
                                   | y == z = removeAll y zs
                                   | otherwise = z : removeAll y zs

-- 3. replace
replace :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
replace _ _ [] = []
replace 0 b (x:xs) = b:xs
replace a b (x:xs) = x : replace (a-1) b xs 
     

-- 4. prereqFor
prereqFor :: Eq t => [(a, [t])] -> t -> [a] 
prereqFor [] _ = []   -- base case
prereqFor (x:xs) listedCourse                                                      
     |listedCourse `exists` getSecond x  = getFirst x : prereqFor xs listedCourse --case 1: when listed course exists in the list of prerequisites
     |otherwise = prereqFor xs listedCourse                                       --case 2: when listed course does not exist. 
               --accessing the tuplet 
               where getFirst :: (a,b) -> a    --retrieve the first element of the tuplet; or course name 
                     getFirst (x,_) = x
                     getSecond :: (a,b) -> b   --retrieve the second element of the tuple; or list of prerequisites
                     getSecond (_,y) = y


-- 5. isPalindrome
isPalindrome :: [Char] -> Bool 
isPalindrome [] = True    -- case for an empty character
isPalindrome x = reverse' (removeSpaceAndCapitalize  x) == removeSpaceAndCapitalize x -- check if the reversed String == the origin 
                   where reverse' :: [a] -> [a]                       --reverse String function 
                         reverse' [] = []
                         reverse' (x:xs) = x `snoc` (reverse' xs)
                              where snoc x xs = xs ++ [x]     

                         removeSpaceAndCapitalize :: String -> String --remove space and capitalize every character 
                         removeSpaceAndCapitalize [] = []
                         removeSpaceAndCapitalize (x:xs) 
                              |x == ' ' = removeSpaceAndCapitalize xs 
                              |otherwise = toUpper x: removeSpaceAndCapitalize xs


-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]
groupSumtoN n lst = 
     reverse(groupSumHelper n lst [])           -- reverse the list for correct order 
     where
          groupSumHelper :: (Ord a, Num a) => a -> [a] -> [[a]] -> [[a]]
          groupSumHelper _ [] result = reverseDoubleList result            --base case 
                              where reverseDoubleList :: [[a]] -> [[a]]    -- reverse the element inside the list of the double list for correct order 
                                    reverseDoubleList [] = []
                                    reverseDoubleList (x:xs) = reverseList x : reverseDoubleList xs
                                        where
                                             reverseList :: [a] -> [a]
                                             reverseList [] = []
                                             reverseList (y:ys) = reverseList ys ++ [y]

          groupSumHelper n (x:xs) [] = groupSumHelper n xs [[x]] 
          groupSumHelper n (x:xs) (ys:result)
               | x > n = groupSumHelper n xs ([x] : ys : result)            --case 1
               | sum ys + x <= n = groupSumHelper n xs ((x:ys) : result)    --case 2 
               | otherwise = groupSumHelper n (x:xs) ([]:ys:result)         --case 3 
