#6: Sorting: Triangle

A_1 = [10,2,5,1,8,20]
A_2 = [10,50,5,1]
A_3 = [-4,-5,-2]

def solution(A):
    A = [x for x in A if x > 0]
    
    if(len(A)<3):
        return 0
    
    B = sorted(A)
    for i in range(len(B)-2):
        if((B[i] + B[i+1] > B[i+2]) & (B[i] < B[i+1] + B[i+2]) & (B[i] + B[i+2] > B[i+1])):
            return 1
    return 0
    
print(solution(A_1))