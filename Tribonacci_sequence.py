"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of
the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers
trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1,1,1] as a starting input (AKA signature), we have this sequence:
{1,1,1,3,5,9,17,31,...}

But what if we started with [0,0,1] as a signature? As starting with [0,1] instead of [1,1] basically shifts the common
Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places,
but that is not the case and we would get:

{0,0,1,1,2,4,7,13,24,...}
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature
array/list, returns the first n elements - signature included of the so seeded sequence.
"""

# TODO


def tribonacci(signature,n):
    #your code here




print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([0, 1, 1], 10))
print(tribonacci([1, 0, 0], 10))
print(tribonacci([0, 0, 0], 10))
print(tribonacci([1, 2, 3], 10))
print(tribonacci([3, 2, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([300, 200, 100])
print(tribonacci([0.5, 0.5, 0.5])