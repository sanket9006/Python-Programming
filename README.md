# <p align="center"> Python Programming</p>

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

# <p align="center"> -X-X-X </p>

> Question 2

Write a program which can compute the factorial of a given numbers.

Solution:

    def fact(x):
      if x==1:
        return 1
      return x*fact(x-1)

    y=int(input())
    print(fact(y))
    
# <p align="center"> -X-X-X </p>

> Question 3

Write a program to generate a dictionary that contains (i, i*)

Solution:

    p={}
    n=int(input())
    for i in range (1,n+1):
      p[str(i)]=str(i*i)
    print(" ".join(p))
    pp=p.values()
    print(" ".join(pp))
    
Output

    10
    1 2 3 4 5 6 7 8 9 10
    1 4 9 16 25 36 49 64 81 100
    
# <p align="center"> -X-X-X </p>    
    
> Question 4  

Write a program to check if two strings are anagram

Solution:

    a="ababa" #string 1
    b="ababa" #string 2
 
    print(anagram(a,b))

