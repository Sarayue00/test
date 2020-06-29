import math


def Data(sample):   
    sample = sample.replace(" ",",")
    data = eval(sample)
    return data

def NP_dot(a,b,m,n):
    S = []
    for i in range (m):
        s = 0
        for j in range (n):
            s += a[n*i+j] * b[j]
        S.append(s)
    return S

def NP_maximum(a):
    b = []
    for item in a:
        if item >= 0:
            b.append(item)
        else:
            b.append(0)
    return b

def Max_broadcast(a,m):
    b = []
    for i in range(m):
        b.append(a[i] - max(a))
    return b

def softmax(x):
    x = Max_broadcast(x,10)
    a = []
    for item in x:
        exp_x = math.exp(item)
        a.append(exp_x)
    s = sum(a)
    b = []
    for item in a:
        softmax_x = item / s
        b.append(softmax_x)   
    return b

def outMaxIndex(a):
    max_value = 0
    max_i = 0
    for i in range(len(a)) :
        if a[i] > max_value:
            max_value = a[i]
            if max_value == max(a):
                max_i = i
    return(max_i+1)
    
def outY(x,w1,w2,m,n):
    a = NP_dot(w1,x,m,n)
    ReLU_a = NP_maximum(a)
    z = NP_dot(w2,ReLU_a,10,m)
    y = softmax(z)
    y_max_index = outMaxIndex(y)  
    return y,y_max_index


def ChangeX(x0,x1):
    x_change = []
    x0 = list(x0[0])
    x1 = list(x1[0])
    for i in range(len(x0)):
        x0 = x1[:]
        for j in range(-128,128):
            x0[i] = j
            x_change.append(x0[:])  
            if x1[:] in x_change:
                x_change.remove(x1[:])
    return x_change

  
def Situation1(x,w1,w2,m,n,y_max_index):
    y_final_max = 0 
    for item in x:
        y_final,y_final_max_index = outY(item,w1,w2,m,n) 
        if y_final_max_index != y_max_index :
            if max(y_final) > y_final_max :
                y_final_max = max(y_final)
                x_final = item
                #y_final_index = y_final_max_index
            
    return x_final
    
    
if __name__ == '__main__':
    N,M = Data(input())
    X = Data(input())
    W1 = Data(input())
    W2 = Data(input())
    y,y_max_index= outY(X,W1,W2,M,N)
   

    if N and M not in range(1,101):
        print("Data exception")
    for x in X:        
        if x not in range(-128,128):
            print("Data exception")
    
    X_list = [X].copy()
    
    X_change = ChangeX(X_list,[X])
    x_final= Situation1(X_change,W1,W2,M,N,y_max_index)
    for i in range(N):
        if x_final[i] != X[i]:
            print(i+1,x_final[i])
     
    

        


