import Data.List
import Data.Char

chainTerminus :: Int -> Int
chainTerminus 1 = 1
chainTerminus 89 = 89
chainTerminus n
  | n <= 0    = -1
  | otherwise = chainTerminus $ sum $ map ((\x -> x*x) . digitToInt) $ show n

main = do putStrLn $ show $ length $ filter (==89) $ map chainTerminus [1..10000000]

