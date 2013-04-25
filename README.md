HW2 and HW3
===
Jessica Junk
Math 480


The fibonacci.py file asks the user to input a positive integer
and returns the Fibonacci Sequence up through that nth number.

Examples:

find_fib(4)   --> 2
find_fib(7)   --> 8

for i in range(1, 11):
  print find_fib(i)
  Here are the first 10 numbers in the Fibonacci Sequence:                                                                                                                 
0                                                                                                                                                                        
1                                                                                                                                                                        
1                                                                                                                                                                        
2                                                                                                                                                                        
3                                                                                                                                                                        
5                                                                                                                                                                        
8                                                                                                                                                                        
13                                                                                                                                                                       
21                                                                                                                                                                       
34                            

HW3:
original hw2 code: timeit("find_fib(1000)") --> 625 loops, best of 3: 271 µs per loop
revised hw3 code:  timeit("find_fib(1000)") --> 625 loops, best of 3: 127 µs per loop
