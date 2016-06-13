import Data.List

divisible :: Integer -> Integer -> Bool
divisible n x = n `mod` x == 0

lessThanSqrt :: Integer -> Integer -> Bool
lessThanSqrt n x = x*x <= n

eratosthenes :: Integer -> [Integer]
eratosthenes n = foldr (\i acc -> i:(filterIfLessThanSqrt i acc)) [] (2:[3,5..n])
  where
  filterIfLessThanSqrt i acc
    | lessThanSqrt n i = filter (\x -> not (divisible x i)) acc
    | otherwise = acc

main = do putStrLn $ show $ sum $ eratosthenes 2000000
