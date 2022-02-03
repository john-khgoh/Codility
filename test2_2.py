#2: Arrays: OddOccurencesInArray

#from time import sleep

A = [9,3,9,3,9,7,9]
#A = [9,5,1,5,1,3,7,3,9]
'''
def solution(A):
    B = []
    A_set = list(set(A))
    #B = list(filter(lambda x:A.count(x)<=1,A))
    for i in A_set:
        if(A.count(i)<=1): #If it has less than one occurence
            B.append(i)
    return B[0]

def solution(A):
    for i in 
'''

'''
def solution(A):             
    A_dict = {}
    while(1):
        #sleep(1)
        #print(A,A_dict)
        if(len(A)==1):
            return A[0]
        for i in A:
            #print(i)
            try: #Element has already been seen
                A_dict[i] += 1 
                A = [x for x in A if x != i] #Eliminate all of element that has been seen
                del A_dict[i] #Eliminate k,v pair from dictionary
                break
            except: #Element has not been seen
                A_dict[i] = 1 # 
    for k,v in A_dict.items():
        return k
'''
'''
import pandas as pd

def solution(A):
    len_A = len(A)
    B = [1] * len(A)
    
    A_df = pd.DataFrame(A,columns=['no'])
    B_df = pd.DataFrame(B,columns=['count'])
    A_df = pd.concat([A_df,B_df],axis=1)
    A_df = A_df.groupby(['no']).size().reset_index(name='count')
    return A_df[A_df['count']==1]['no'].values[0]
'''
from collections import Counter

def solution(A):
    counts = Counter(A)
    return (list(counts.keys())[list(counts.values()).index(1)]) 
    
print(solution(A))