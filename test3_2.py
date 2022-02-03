#3: Time Complexity: PermMissingElement

'''
import sys

def solution(A):
    if(not bool(A)):
        return 1
    elif(len(A)==1):
        return A[0] + 1
    try:
        max_A = max(A) + 1
        B = list(range(1,max_A)) 
        
        missing = [x for x in B if x not in A]
        return(missing[0])
    except:
        sys.exit(1)
'''        
def solution(A):
    if(not bool(A)):
        return 1
    elif(len(A)==1):
        return A[0] + 1
    
    try:
        max_A = max(A)
        max_A_1 = max_A + 1
        #print(max_A,max_A_1)
        result = max_A * (max_A_1) // 2 - sum(A)
        return result
    except:
        sys.exit(1)
    
A = [1,2,3,5]
#print(solution(A))

print(solution(A))