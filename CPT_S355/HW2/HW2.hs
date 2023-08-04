-- CptS 355 - Summer 2023 Assignment 2
-- Name: Dao Minh Triet 
-- ID: 011753385
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Fuse foldr/map" #-}
{-# HLINT ignore "Use sum" #-}
{-# HLINT ignore "Eta reduce" #-}

module HW2
     where

{- 1-  merge2 & merge2Tail & mergeN - 22% -}
--merge2
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] b = b
merge2 a [] = a
merge2 (x:xs) (y:ys)
     | x <= y = x : merge2 xs (y:ys)
     | otherwise = y : merge2 (x:xs) ys

--merge2Tail
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail a b = tailHelper a b []
                where
                     tailHelper :: Ord a => [a] -> [a] -> [a] -> [a]
                     tailHelper [] b c =  c `revAppend` b
                     tailHelper a [] c =  c `revAppend` a
                     tailHelper (a:as) (b:bs) c
                        |a <= b = tailHelper as (b:bs) (a:c)
                        |otherwise = tailHelper (a:as) bs (b:c)
                     revAppend :: [a] -> [a] -> [a]
                     revAppend [] acc = acc
                     revAppend (x:xs) acc = revAppend xs (x:acc)

--mergeN
mergeN :: Ord a => [[a]] -> [a]
mergeN x = foldr merge2 [] x

{- 2 - getInRange & countInRange - 18% -}
--getInRange
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange x y ls = filter (isInRange x y) ls
               where isInRange x y num = x < num && num < y

--countInRange
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange x y z = foldr (+) 0 ( map (countHelper x y) z )
               where countHelper x y z = length (getInRange x y z)

{- 3 -  addLengths & addAllLengths - 18% -}
-- addLengths
data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int
                   deriving (Show, Read, Eq)
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths a b = INCH (convert a + convert b)
               where
                     convert ::  LengthUnit -> Int
                     convert (INCH x) = x
                     convert (FOOT x) = 12*x
                     convert (YARD x) = 36*x

-- addAllLengths
addAllLengths :: [[LengthUnit]] -> LengthUnit
addAllLengths x = foldr addLengths (INCH 0) (map (foldr addLengths (INCH 0)) x)

{-4 - sumTree and createSumTree - 22%-}
data Tree a = LEAF a | NODE a  (Tree a)  (Tree a)
              deriving (Show, Read, Eq)
--sumTree
sumTree :: Num p => Tree p -> p
sumTree (LEAF a) = a
sumTree (NODE a x y) = sumTree x + sumTree y

--createSumTree
createSumTree :: Num a => Tree a -> Tree a
createSumTree (LEAF a) = LEAF a
createSumTree (NODE a x y)  =  NODE (sumTree x + sumTree y) (createSumTree x) (createSumTree y)

{-5 - foldListTree - 20%-}
data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
                  deriving (Show, Read, Eq)
foldListTree :: (a -> a -> a) -> a -> ListTree a -> a
foldListTree op base (ListLEAF []) = base
foldListTree op base (ListNODE []) = base
foldListTree op base (ListNODE (x:xs) ) = foldl op base (preOrderTri x) `op` (foldListTree op base (ListNODE xs))
               where preOrderTri :: ListTree a -> [a]
                     preOrderTri (ListLEAF x) = x
                     preOrderTri (ListNODE []) = []
                     preOrderTri (ListNODE (x:xs)) =  preOrderTri x ++ preOrderTri (ListNODE xs)

{- 6- Create two tree values :  Tree Integer  and  listTree a ;  Both trees should have at least 3 levels. -}
  