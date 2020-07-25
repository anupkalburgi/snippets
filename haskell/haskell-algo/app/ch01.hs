module Ch01 where

type Nat = Int

length' :: [a] -> Nat
length' [] = 0
length' (x : xs) = 1 + length' xs

map' :: (a -> b) -> [a] -> [b]
map' f [] = []
map' f (x:xs) = f x : map' f xs

filter' :: (a -> Bool) -> [a] -> [a]
filter' f [] = []
filter' f (x:xs) = if f x then x : filter' f xs else filter f xs 

foldr' :: (a -> b -> b) -> b -> [a] -> b
