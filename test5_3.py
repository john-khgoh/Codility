#5: Prefix Sum: GenomicRangeQuery

#ACGT

S = 'CAGCCTA'
P = [2,5,0]
Q = [4,5,6]

import re

def solution(S, P, Q):
    result = []
    
    PQ = list(zip(P,Q))
    for i in PQ:
        start = i[0]
        stop = i[1] + 1
        sub_S = S[start:stop]
        if(re.search('A',sub_S)):
            result.append(1)
        elif(re.search('C',sub_S)):
            result.append(2)
        elif(re.search('G',sub_S)):
            result.append(3)
        else:
            result.append(4)
    return result
    
print(solution(S, P, Q))