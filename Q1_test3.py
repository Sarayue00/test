def Data(sample):   
    sample = sample.replace(" ",",")
    data = eval(sample)
    return data

def outputMixedNum(w,s,X,W,P):
    x = P//s
    if P % s == w:
        x += 1   
    for i in range(100):
        if s*i+w <= X < s*(i+1)+w:
            a = s*(i+1)
        if X+W > P:
            W = P-X
        if s*i < X+W <= s*(i+1):
            if i < x:
                b = s*(i+1)
            else:
                b = s*x
    return (b-a)/s 

if __name__ == '__main__':
    w,h,s,t,k,P,Q = Data(input())  
    S = 0
    for i in range(k):
        X,Y,W,H = Data(input())
        c = outputMixedNum(w,s,X,W,P)
        d = outputMixedNum(h,t,Y,H,Q)
        S += int(c*d)
    print(S)