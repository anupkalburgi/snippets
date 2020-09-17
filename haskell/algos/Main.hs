module Main where


main :: IO ()
main = putStrLn "this"


-- length :: Num p => [a] -> p
-- length [] = 0

type Nat = Int

label :: [a] -> [(Nat, a)]
label xs = zip [0..] xs

length :: [a] -> Nat
length xs = foldr succ 0 xs where succ x n = n + 1

concat1, cantcat2 :: [[a]] -> [a]
concat1 = foldr (++) []
cantcat2 = foldl (++) []

inserts :: a -> [a] -> [[a]]
inserts x [] = [[x]]
inserts x (y:ys) = (x:y:ys): map (y:) (inserts x ys)

perms :: [a] -> [[a]]
perms [] = [[]]
perms (x:xs) = [zs | ys <- perms xs , zs <- inserts x ys]

perms1 :: [a] -> [[a]]
perms1 xs = foldr step [[]]  xs 
    where step x xss = concatMap (inserts x) xss

concatMap1 :: (a -> [b]) -> [a] -> [b]
concatMap1 f xs  =  concat $ map f xs

perms2 :: [a] -> [[a]]
perms2 [] =  [[]]
perms2 xs = [x : zs | (x, ys) <- picks xs , zs <- perms2 ys ]
-- Pick the first element, and then get the permutations of rest of the list and add to the 1st element


picks :: [a] -> [(a, [a])]
picks [] = []
picks (x:xs) = (x,xs) : [(y, x:ys) | (y, ys) <- picks xs]

-- perms2' :: [a] -> [[a]]
perms2' [] = [[]]
perms2' xs = concatMap subperms (picks xs)
                where  subperms (x,ys) = map(x:) (perms2' ys)


-- test f e = foldr f e (concat [[1],[2]])

-- tmp :: String -> Int -> String
tmp a = id . ( [1,2,3] ++)
