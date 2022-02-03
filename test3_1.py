#3: Time Complexity: Frogjmp

import math

def solution(X,Y,D):
    distance = Y - X
    no_of_jumps = math.ceil(distance/D)
    return no_of_jumps
    
print(solution(0,100,49))