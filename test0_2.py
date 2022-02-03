'''
answer = [0,0,0,0,0]
B = [2,4,4,5]

def normal_counter(answer,B):
    for j in B:
        answer[j-1] += 1
    return answer
    
print(normal_counter(answer,B))
'''

#A = [2,1,1,2,1,5,1,2,1]
#A_str = ''.join(map(str, A))

from collections import Counter

def max_counter(answer,B):
    #print("Max:%s" %B)
    #print(answer)
    count_dictionary = Counter(B)
    max_count = int(count_dictionary[max(count_dictionary, key=count_dictionary.get)])
    len_answer = len(answer)
    new_answer = [max_count] * len_answer
    sum_answer = [answer + new_answer for answer,new_answer in zip(answer,new_answer)]
    #print(sum_answer)
    return sum_answer

def normal_counter(answer,B):
    B = list(B) #Convert B from string to list
    B = list(map(lambda x:int(x),B)) #Convert elements in B from str to int
    #print(B)
    #print(answer)
    #print(len(B))
    #print("Normal:%s" %B)
    for m in B:
        answer[m-1] += 1
    #print(answer)
    return answer
    
#greater_set_list = [2,5]

#Convert elements of greater_set_list from int into string
#

#N = 1
#A_str = '211215121'

def solution(N,A):
    #N = 5
    #A_str = '3446144'
    answer = [0] * N
    #B_list_new = []
    #B = A.split('2')
    
    try:
        #Check if there's a value that's greater than N
        greater_list = [x for x in A if x > N]
        greater_set_list = list(set(greater_list))
        greater_set_list = list(map(lambda x:str(x),greater_set_list))
        
        A_str = ''.join(map(str, A))
        for i in greater_set_list:
            placeholder = str(i) + "/"
            A_str = A_str.replace(str(i),placeholder)
            B_list = A_str.split("/")
    except Exception as e:
        return e
    
    #Remove blankspaces from B_list
    try:
        B_list.pop(B_list.index(''))
    except:
        pass
    #print(greater_set_list)
    #print(B_list)
    if(len(greater_list)>0):
        #Search for elements of greater_set_list within elements of B_list
        for j in B_list:
            or_flag = 0
            for k in greater_set_list:
                if(k in j):
                    or_flag = 1
            #The or_flag represents the presence of greater_set_list elements in j string
            if(or_flag==1):
                #Checks if a j string begins with other non-greater_set_list elements
                if(bool(j[:-1])):
                    answer = max_counter(answer,j[:-1])
                else:
                    #Nothing to do here since there's no preceeding values
                    pass
            else:
                answer = normal_counter(answer,j)
            #print(answer)
    else: #Otherwise perform operation from A[0]
        answer = normal_counter(answer,A)
    return answer

#N = 1
#A = [2,1,1,2,1,5,1,2,1]   

N = 4
A = [3,1,2,4,1,1,5,1]
print(solution(N,A))