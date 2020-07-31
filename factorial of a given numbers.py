def fact(x):
  if x==1:
    return 1
  return x*fact(x-1)

y=int(input())
print(fact(y))