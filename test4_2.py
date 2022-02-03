#4: Counting Elements: PermCheck

A = [1,2,3,4]

def solution(A):
    #if(len(A)<=1):
    #    raise Exception('Array length must be greater than one')
    try:
        max_A = max(A)
        total_A = sum(A)
        #print(total_A)
        expected_A = sum(list(range(1,max_A+1)))
        #expected_A = sum(list()))
        #print(expected_A)
        if(abs(expected_A - total_A)==0):
            return 1
        else:
            return 0
    except Exception as e:
        return e
    
print(solution(A))
