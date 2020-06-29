def Data(sample):   
    sample = sample.replace(" ",",")
    data = eval(sample)
    return data

def outPriorsAnchor(W,H,S,T,P,Q):
    Prior_xy = []
    x = P//S
    y = Q//T
    if P % S == W:
        x += 1
    if Q % T == H:
        y += 1
    for j in range(y):   
        for i in range(x):            
            Prior_x = S * i
            Prior_y = T * j
            Prior_xy.append([Prior_x,Prior_y])            
    return Prior_xy

def Mixed_xy(rec1,rec2):
    left_column_max  = max(rec1[0],rec2[0])
    right_column_min = min(rec1[2],rec2[2])
    up_row_max       = max(rec1[1],rec2[1])
    down_row_min     = min(rec1[3],rec2[3])
    if left_column_max>=right_column_min or down_row_min<=up_row_max:
        return 0
    else:
        return rec2[0],rec2[1]

if __name__ == '__main__':
    w,h,s,t,k,P,Q = Data(input())  
    if P and Q not in range(1,1001):
        False
    if w and h and s and t not in range(1,101):
        False 
    prior_anchors = outPriorsAnchor(w,h,s,t,P,Q)
    M_xy = []
    for i in range(k):
        X,Y,W,H = Data(input())
        if 0<=X<=P-1 and 0<=Y<=Q-1:
            True
        if W and H not in range(1,501): 
            False  
        rec1 = [X,Y,X+W,Y+H]
        for Anchor in prior_anchors:
            rec2 = [Anchor[0],Anchor[1],Anchor[0]+w,Anchor[1]+h]
            m_xy = Mixed_xy(rec1,rec2)
            if m_xy == 0:
                m = m_xy
            else:
                M_xy.append(m_xy)
    resultList = []
    for xy in M_xy:
        if xy not in resultList:
            resultList.append(xy)
    
    print(len(resultList))