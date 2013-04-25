"""This function takes in an int n and returns the nth number in the
Fibonacci Sequence, where the sequence starts with 0, 1, 1, 2, ..."""

%cython
def find_fib2(long n):
    if n > 0:
        if n < 3:
            return n - 1
        else:
            count = 2
            last = 0
            sum = 1
            while count < n:
                count += 1
                hold = sum
                sum += last
                last = hold
            return sum
    else:
        raise ValueError("n must be a positive integer.")

if __name__ == '__main__':
    x = int(raw_input("Input a positive integer: "))
    print "Here are the first %d numbers in the Fibonacci Sequence:" % x
    for i in range(x):
        print find_fib(i + 1)
