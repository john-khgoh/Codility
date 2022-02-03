from collections import Counter

A = [9,3,9,3,9,7,9]

'''
temp_idx = A.index(7)
print(temp_idx)
print(A[temp_idx:])
'''
'''
def solution(A):
    counts = Counter(A)
    #return (list(counts.keys())[list(counts.values()).index(1)]) 
    return counts[max(counts, key=counts.get)]
    
print(solution(A))
'''