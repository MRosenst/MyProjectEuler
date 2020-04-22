import Data.List

main = print solution

solution :: Int
solution = read $ sort (permutations "0123456789") !! 999999
