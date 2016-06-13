import Data.List

isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome xs = xs == (reverse xs)

descendingUniqueProducts :: Int -> Int -> [Int]
descendingUniqueProducts x y = sortBy (flip compare) $ nub [a*b | a <- [x,x-1..1], b <- [y,y-1..1]]

main = do putStrLn $ show $ head $ filter (\x -> isPalindrome $ show x) $ descendingUniqueProducts 100 100
