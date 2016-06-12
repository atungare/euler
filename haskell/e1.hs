import Data.List

sumMultiples :: Int -> [Int] -> Int
sumMultiples lim preds = sum $ filter checkPreds [1..maxVal]
  where checkPreds n = any (\x -> n `mod` x == 0) preds
        maxVal = lim - 1

main = do putStrLn $ show $ sumMultiples 1000 [3, 5]
