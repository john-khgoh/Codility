#6: Sorting: Distinct

A = [2,1,1,2,3,1]

def solution(A):
    A_set = list(set(A))
    return len(A_set)
    
print(solution(A))