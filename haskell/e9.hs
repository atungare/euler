import Data.List

tripleFinder :: Int -> [[Int]]
tripleFinder n = [[a,b,c] | a <- [1..n], b <- [1..n], c <- [n-a-b], a*a + b*b == c*c]

main = do putStrLn $ show $ product $ head $ tripleFinder 1000

