#2: Arrays: CyclicRotation

import unittest

def solution(A, K):
    B = A[-K:]
    C = A[:-K]
    A = B + C
    return (A)

A = [-1, -2, -3, -4]
K = 1    
print(solution(A,K))
