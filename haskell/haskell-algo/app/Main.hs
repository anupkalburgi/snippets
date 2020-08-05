module SubSet where

import Lib
import Data.List (unwords)


-- main :: IO ()
-- main = someFunc

example :: [String]
example = ["this", "is", "madness"]


nms :: [a] -> a -> [a]
nms x y = x ++ [y]


subset :: [a] -> [[a]]
subset (a : []) = [[a]]
subset (x : xs) = (map (\a -> a ++ [x]) (subset xs)) ++ [[x]] ++ (subset xs)