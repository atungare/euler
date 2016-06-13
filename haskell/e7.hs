import Data.List

sieve :: [Integer] -> [Integer]
sieve (seed:xs) = seed : sieve [x | x <- xs, x `mod` seed /= 0]

naiveSieve :: [Integer]
naiveSieve = sieve [2..]

sixKPlusMinus1 :: [Integer]
sixKPlusMinus1 = 2:3:(sieve [x | x <- concatMap (\x -> [6*x-1,6*x+1]) [1..]])

main = do putStrLn $ show $ take 10001 sixKPlusMinus1
