# Rabbits and Recurrence Relations

# Problem
# A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat.
# Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…).
# We use the notation "an" to represent the n-th term of a sequence.

# A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. 
# A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior.
# As a result, if Fn represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). 
# Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

# When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n.
# This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
# print(path.dirname(path.dirname(path.dirname(path.realpath(__file__)))))
from dna_toolset.decorate import *

@timeit # Comes from decorate.py
def recusive_fibonacci_rabbits_version_1(num_months, num_offspring):
    '''V1: A recursive function that determines the population of rabbits after num_months months when each litter results in num_offspring offspring'''

    if num_months == 1:
        return 1
    elif num_months == 2:
        return num_offspring
    
    one_generation = recusive_fibonacci_rabbits_version_1(num_months-1, num_offspring)
    two_generations = recusive_fibonacci_rabbits_version_1(num_months-2, num_offspring)
    
    if num_months <= 4:
        return one_generation + two_generations
    
    return one_generation + (two_generations * num_offspring)

part_header("recusive_fibonacci_rabbits: Version 1")
print(recusive_fibonacci_rabbits_version_1(5, 3))
print(recusive_fibonacci_rabbits_version_1(4, 3))

@timeit
def recusive_fibonacci_rabbits_version_2(num_months, num_offspring):
    '''V2: A recursive function that determines the population of rabbits after num_months months when each litter results in num_offspring offspring
    
    A more concise, elegant solution to the problem'''
    # BUT appears to be more time-costly (I guess as we're performing Binary Recursion???)
    if num_months < 2:
        return num_months
    else:
        return recusive_fibonacci_rabbits_version_2(num_months-1, num_offspring) + recusive_fibonacci_rabbits_version_2(num_months-2, num_offspring) * num_offspring 

part_header("recusive_fibonacci_rabbits: Version 2")
print(recusive_fibonacci_rabbits_version_2(5, 3))
print(recusive_fibonacci_rabbits_version_2(4, 3))

@timeit
def iterative_fibonacci_rabbits(num_months, num_offspring):
    '''An iterative solution to the fibonacci rabbits problem. Determines the population of rabbits after num_months months when each litter results in num_offspring offspring'''
    # Appears to be the fastest!!!
    fn_1, fn_2 = 1, 1
    fn = 1  # Just a placeholder in case n is too small
    for _ in range(2, num_months):
        fn = fn_1 + fn_2 * num_offspring
        fn_2, fn_1 = fn_1, fn
    return fn

part_header("iterative_fibonacci_rabbits")
print(iterative_fibonacci_rabbits(5, 3))
print(iterative_fibonacci_rabbits(4, 3))