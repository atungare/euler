import Data.List

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome xs = xs == (reverse xs)

uniquePalindromes :: Int  -> [Int]
uniquePalindromes x = nub [a*b | a <- [x,x-1..1], b <- [a,a-1..1], isPalindrome (show (a*b))]

main = do putStrLn $ show  $ head $ sortBy (flip compare) $ uniquePalindromes 999
