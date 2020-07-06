linear x = x
sigmoid x = 1/(1+exp(x))
mysin x = sin x

rectify f x =
  if x > 0 then f x else 0

main = print(rectify mysin (3))
