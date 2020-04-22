import Debug.Trace
f x = traceShow x x

main = print solution

factSum :: Int -> Int
factSum = sum . map (fact . read . pure) . show
    where
        fact = product . enumFromTo 1

curious :: Int -> Bool
curious n = n == factSum n

solution :: Int
solution = sum . f . filter curious $ [10..1000000]
