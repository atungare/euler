import Data.List

divisible :: Integer -> Integer -> Bool
divisible n x = n `mod` x == 0

divisors :: Integer -> [Integer]
divisors n = foldl (\acc x -> (foldr strikeDivisor x acc):acc) [] [2..n]
  where strikeDivisor y i = if divisible i y then (div i y) else i

main = do putStrLn $ show $ product $ divisors 20


