#6: Sorting: MaxProductOfThree

A_1 = [-3,1,2,-2,5,6]
A_2 = [-4,-5,-1,0,1,2,5,10]

def solution(A):
    A_sorted = sorted(A)
    #print(A_sorted) 
    considered_numbers = []
    B = A_sorted[-1:][0] * A_sorted[-2:][0] * A_sorted[-3:][0]
    C = A_sorted[-1:][0] * A_sorted[0:][0] * A_sorted[1:2][0]
    
    return max([B,C])
print(solution(A_2))