#4: Counting Elements: MissingInteger

A_1 = [-1,2,3,5,1,6] #Answer:0
A_2 = [-4,-3,-2] #Answer:1
A_3 = [-3,-2,-1,0,1] #Answer:2
A_4 = [4] #Answer:1
A_5 = [-4] #Answer: 1
A_6 = [-3,-2,-1,0,1,2] #Answer:3

def solution(A):
    #Check if the largest no. is less than,equal to 0. If not, return 1
    max_A = max(A)
    min_A = min(A)
    len_A = len(A)
    
    #print(max_A,len_A)
    
    if(max_A<=0):
        #print("flag_1")
        return 1
    elif((len_A==1) & (max_A==1)):
        #print("flag_2")
        return 2
    elif((len_A==1) & (max_A!=1)):
        #print("flag_3")
        return 1
    else:
        #print("flag_4")
        B = list(range(1,max_A))
        A = [x for x in A if x>0]
        #print(A,B)
        try:
            #C = [x for x in B if x not in A]
            C = list(set(B) - set(A))
            #print(C)
            min_C = min(C)
            return min_C
        except:
            return max_A + 1
            
print(solution(A_6))