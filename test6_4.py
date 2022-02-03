#6 :Sorting: NumberOfDiscIntersections
from time import sleep

A = [1,5,2,1,4,0]

def solution(A):
    if(len(A)<2):
        return 0

    A_dict = {}
    cnt = 0
    #limit_cnt = 0
    #intersect_list = []
    intersection_cnt = 0
    
    for i in A:
        A_dict[cnt] = [cnt-i,cnt+i] 
        cnt += 1
    
    B_dict = dict(sorted(A_dict.items(), key=lambda item: item[1])) #Circles sorted by left-most position
    B_dict = {i: v for i, v in enumerate(B_dict.values())} #Reindex circles
    
    print(B_dict)
    #Iterating by circle i
    for i in range(len(B_dict)):
        #Comparing against circle i + cnt until no intersection, then break
        for j in range(i+1,len(B_dict)):
            #print(B_dict[i],B_dict[j])
            if(intersection_cnt>10000000):
                return -1
            '''
            if(B_dict[i][0]==B_dict[i][1]):
                BDI_range = [B_dict[i][0]]
            else:
                BDI_range = list(range(B_dict[i][0],B_dict[i][1]))
            
            if(B_dict[j][0]==B_dict[j][1]):
                BDJ_range = [B_dict[j][0]]
            else:    
                BDJ_range = list(range(B_dict[j][0],B_dict[j][1]))
            '''
            
            BDI_range = list(range(B_dict[i][0],B_dict[i][1]+1))
            BDJ_range = list(range(B_dict[j][0],B_dict[j][1]+1))
                        
            intersection = list(set(BDI_range) & set(BDJ_range))
            #print(i,j,intersection)
            if(len(intersection)>0):
                #intersect_list.append((i,j))
                intersection_cnt += 1
                #limit_cnt += 1
            '''
    return intersection_cnt
print(solution(A))