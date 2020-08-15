module Main where

import Lib
import Data.List (unwords)


main :: IO ()
main = someFunc

example :: [String]
example = ["this", "is", "madness"]


nms :: [a] -> a -> [a]
nms x y = x ++ [y]


add :: String -> String -> Int
add s1 s2 = 10

subset :: [a] -> [[a]]
subset (a : []) = [[a]]
subset (x : xs) = (map (\a -> a ++ [x]) (subset xs)) ++ [[x]] ++ (subset xs)


-- insertionSort :: [a] -> [a]
-- insertionSort (a : []) = [a]
-- insertionSort xsl = insert 