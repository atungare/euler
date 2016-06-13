import Data.List

tripleFinder :: Int -> [[Int]]
tripleFinder n = [[a,b,c] |  l <- [div n 2], a <- [1..l], b <- [1..l], c <- [n-a-b], a*a + b*b == c*c, b >= a]

main = do putStrLn $ show $ maximumBy (\(_,a) (_,b) -> compare a b) $ map (\x -> (x, (length . tripleFinder) x)) [1..1000]

