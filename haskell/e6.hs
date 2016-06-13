import Data.List

sumSquareDifference :: Integer -> Integer
sumSquareDifference n = squareOfSum - sumOfSquare
  where sumN = sum [1..n]
        squareOfSum = sumN*sumN
        sumOfSquare = sum [x*x | x <- [1..n]]

main = do putStrLn $ show $ sumSquareDifference 100
