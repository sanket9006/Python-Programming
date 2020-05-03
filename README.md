# <p align="center"> Python-Programming</p>

Question 1

                Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
                The numbers obtained should be printed in a comma-separated sequence on a single line.

Solution:
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))

> 2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149......


# Python String join() Method 
