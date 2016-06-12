import Data.List

fibs :: [Int]
fibs = map fst $ iterate (\(x, y) -> (y, x+y)) (0, 1)

sumEvenFibs :: Int -> Int
sumEvenFibs lim = sum $ filter (\n -> n `mod` 2 == 0) $ takeWhile (<lim) fibs

main = do putStrLn $ show $ sumEvenFibs 4000000
