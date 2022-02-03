#4: Counting Elements: MaxCounters

'''
N = 5
A = [3,4,4,6,1,4,4]
'''

N = 1
#A = [1,1,1,1]
A = [2,1,1,2,1]

from collections import Counter
#from time import sleep

def max_counter(answer,B):
    counts = Counter(B)
    answer = int(counts[max(counts, key=counts.get)])
    return answer
    
def normal_counter(answer,B):
    for j in B:
        answer[j-1] += 1
    return answer
    
def solution(N,A):
    answer = [0] * N
    try:
        #Check if there's a value that's greater than N
        greater_list = [x for x in A if x > N] 
        #greater_len = len(greater_list)
        #print(greater_list)
    except Exception as e:
        return e
    #If true, evaluate values up to maximum value
    if(len(greater_list)>0): 
        #last_greater = greater_list[-1:][0]
        #last_greater_index = A.index(last_greater)
        greater_set_list = list(set(greater_list))
        print(A)
        '''
        A_str = ''.join(map(str, A))
        for i in greater_set_list:
            placeholder = "/" + str(i) + "/"
            A_str = A_str.replace(str(i),placeholder)
            B_list = A_str.split("/")
        B_list.pop(B_list.index(''))
        #B_list = list(map(lambda x:int(x),B_list))
        print(B_list)
        '''
    else: #Otherwise perform operation from A[0]
        answer = normal_counter(answer,A)
    return answer
    
print(solution(N,A))

############################################################
'''
            temp_idx = A.index(i)
            if(temp_idx==0):
                pass
            elif(temp_idx>0):
                B = A[:temp_idx]
                answer = [max_counter(B)] * N
            C = A[(temp_idx)+1:] 
        
        answer = normal_counter(answer,C)
        '''