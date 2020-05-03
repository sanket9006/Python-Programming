# <p align="center"> Python-Programming</p>

> Question 1

                Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
                The numbers obtained should be printed in a comma-separated sequence on a single line.

Solution:
              
    l=[]
    for i in range(2000, 3201):
        if (i%7==0) and (i%5!=0):
            l.append(str(i))
    print (','.join(l))


> Question 2

Write a program which can compute the factorial of a given numbers.

Solution:

    def fact(x):
      if x==1:
        return 1
      return x*fact(x-1)

    y=int(input())
    print(fact(y))
    



