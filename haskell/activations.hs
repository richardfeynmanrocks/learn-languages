main =
  linear = \x -> x
  rectify linear

rectify func =
  \func -> case () of
       _ | x > 0 -> func x
         | otherwise -> 0
