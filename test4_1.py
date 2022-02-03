#4: Counting Elements: FrogRiverOne

#A = [3]
#A = [2,1,4,3,1]
A = [1,3,1,4,2,3,5,4]
X = 5

#import sys
'''
def solution(X,A):
    #return int(A.index(X))
    answer_list = []
    
    if(X in A is False):
        return -1
    
    try:
        for i in range(1,X+1):
            answer_list.append(A.index(i))
        return max(answer_list)
    except:
        return -1
'''
def solution(X,A):
    if(X in A is False):
        return -1
    
    answer_list = list(range(1,X+1))
    
    cnt = 0
    for i in A:
        if(i in answer_list):
            answer_list.pop(answer_list.index(i))
        if(len(answer_list)==0):
            break
        cnt += 1
    if(len(answer_list)>0):
        return -1
    return cnt
print(solution(X,A))

