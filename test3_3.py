#3: Time Complexity :TapeEquilibrium

from joblib import Parallel, delayed

def fn(x,A):
    first = sum(A[x+1:])
    second = sum(A[:x+1])
    return abs(second-first)

def solution(A):
    len_A = len(A)
    #min_diff = 0
    #result_list = []
    
    result_list = list(map(lambda x:fn(x,A),A))
    '''
    result_list = Parallel(n_jobs=2,verbose=0,prefer='processes'
        )(delayed(fn)(A,x) for x in range(len_A-1))
    
    for i in range(len_A-1):
        first = sum(A[i+1:])
        second = sum(A[:i+1])
        result_list.append(abs(second-first))

        if(result_list.count(0)>0):
            return(0)
    '''
    return min(result_list)
    
A = list(range(1,10000))
print(solution(A))
