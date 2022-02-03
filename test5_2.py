#5: Prefix Sum: CountDiv

#Scenario_1
#A=5 
#B=20 
#K=3 #Answer=3

#Scenario_3
A=1
B=10
K=3

from math import ceil

def solution(A,B,K):
    #Find the largest numerator below or including B
    #Find the largest numerator above or including A
    
    B_div = B//K
    B_below = B_div * K
    #print(B_below)
    
    A_div = ceil(A/K)
    A_above = (A_div * K)
    #print(A_above)
    
    answer = ((B_below - A_above ) // K) + 1
    #print(answer)
    return answer
    
solution(A,B,K)
