#7: Stacks and queues: Brackets
#from time import sleep

def solution(S):
    #A is a temporary list for storing brackets
    A = []
    dict = {'{':'}','}':'{','(':')',')':'(','[':']',']':'['}
    dict_cnt = {'{':0,'}':0,'(':0,')':0,'[':0,']':0}
    
    #len_S = len(S)
    for i in S:
        #If the array is empty, append
        if(len(A)==0):
            A.append(i)
            dict_cnt[i] += 1
        #Does the final entry of A match i, if so delete it from A
        else:
            if(i==dict[A[-1:][0]]):
                del A[-1:]
                dict_cnt[i] += 1
            else:    
                A.append(i)
                dict_cnt[i] += 1
        #If more closing brackets are seen than opening brackets, return 0
        #print(i,"  ==>  ",dict_cnt)
        #sleep(1)
        if((dict_cnt['}']>dict_cnt['{'])|(dict_cnt[']']>dict_cnt['['])|(dict_cnt[')']>dict_cnt['('])):
            return 0
    #print(A)
    if(len(A)>0):
        return 0
    else:
        return 1
print(solution(S))
