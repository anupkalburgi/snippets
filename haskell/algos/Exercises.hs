-- import Debug.Trace.trace
-- Ex: 1.3
wrap :: a -> [a]
wrap a = [a]

unwrap :: [a] -> a
unwrap (x:[]) = x

single :: [a] -> Bool
single (x : []) = True
single _  = False

-- 1.4
-- foldl f z [x1, x2, ..., xn] == (...((z `f` x1) `f` x2) `f`...) `f` xn
rev :: [a] -> [a]
rev xs = foldl (flip (:)) [] xs

tt :: (a -> Bool) -> a -> [a] -> [a]
tt f x [] = []

-- 1.5
-- foldr f z [x1, x2, ..., xn] == x1 `f` (x2 `f` ... (xn `f` z)...)
filterFold :: (a -> Bool) -> [a] -> [a]
-- filterFold f xs = foldr (\x e -> if f x then (x: e) else e) [] xs 
-- filterFold f xs = foldr op [] xs where op x xs = if f x then x : xs else xs
filterFold f = foldr op [] where op x xs = if f x then x : xs else xs

foldrMap :: (a -> b) -> [a] -> [b]
-- foldrMap f xs = foldr (\a e -> (f a) : e ) [] xs
-- foldrMap f xs = fold r op [] xs where op x xs = f x : xs
foldrMap f = foldr op [] where op x xs = f x : xs

takeWhile' :: (a -> Bool) -> [a] -> [a]
-- takeWhile' f xs = foldr op [] xs where op x xs = if f x then x : xs else []
takeWhile' f = foldr op [] where op x xs = if f x then x : xs else []
-- takeWhile even [2,3,4,5]
-- takeWhile op 2 (takeWhile [3,4,5])
-- takeWhile op 2 : op 3 (takeWhile [4,5])
-- takeWhile op 2 : []

dropWhileEnd' :: (a -> Bool) -> [a] -> [a]
dropWhileEnd' p = foldr op [] 
                    where op x xs = if p x && null xs then [] else x:xs