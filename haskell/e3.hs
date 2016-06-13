import Data.List

divisible :: Integer -> Integer -> Bool
divisible n x = n `mod` x == 0

lessThanSqrt :: Integer -> Integer -> Bool
lessThanSqrt n x = x*x <= n

factorPairs :: Integer -> [(Integer, Integer)]
factorPairs n = [(x, div n x) | x <- filter (divisible n) $ takeWhile (lessThanSqrt n) [1..]]

isPrime :: Integer -> Bool
isPrime n = factorPairs n == [(1, n)]

descendingFactors :: Integer -> [Integer]
descendingFactors n = foldr step [] $ factorPairs n
  where step (x, y) acc = y:(acc ++ [x])

main = do putStrLn $ show $ find isPrime $ descendingFactors 600851475143
