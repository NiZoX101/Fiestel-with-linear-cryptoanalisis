from random import randint
from coding import *
S1={
    0:2,
    1:1,
    2:3,
    3:6,
    4:6,
    5:3,
    6:4,
    7:4,
    8:7,
    9:5,
    10:4,
    11:7,
    12:1,
    13:6,
    14:2,
    15:5
    }

S2={
    0:4,
    1:1,
    2:4,
    3:7,
    4:5,
    5:6,
    6:2,
    7:1,
    8:2,
    9:6,
    10:4,
    11:5,
    12:3,
    13:7,
    14:6,
    15:3
    }

S3={
    0:2,
    1:1,
    2:3,
    3:2,
    4:3,
    5:1,
    6:1,
    7:2,
    8:3,
    9:1,
    10:1,
    11:3,
    12:2,
    13:3,
    14:1,
    15:2
    }
P={
    1:3,
    2:4,
    3:1,
    4:2,
    5:6,
    6:8,
    7:5,
    8:7,
    9:3,
    10:8,
    11:2,
    12:4

    }

IP={
    1:8,
    2:7,
    3:3,
    4:2,
    5:5,
    6:4,
    7:1,
    8:6
    }
s1={}
s2={}
s3={}
affective_s1={}
affective_s2={}
affective_s3={}
def analyze_blocks(S):
    s={}
    if S==S1 or S==S2:
        for j in range(1,8):
            for i in range(1,16):
                count=0
                for inp,out in S.items():
                    inp1=inp&i
                    out1=out&j
                    count1=0
                    count2=0
                    for ind in range(0,15):
                        if inp1 & 1<<ind:
                            count1+=1
                    for ind in range(0,7):
                        if out1 & 1<<ind:
                            count2+=1
                    if count1%2==count2%2:
                        count+=1
                s[(i, j)] = count

    elif S==S3:      
        for j in range(1,4):
            for i in range(1,16):
                count=0
                for inp,out in S3.items():
                    inp1=inp&i
                    out1=out&j
                    count1=0
                    count2=0
                    for ind in range(0,15):
                        if inp1 & 1<<ind:
                            count1+=1
                    for ind in range(0,3):
                        if out1 & 1<<ind:
                            count2+=1
                    if count1%2==count2%2:
                        count+=1
                s[(i, j)] = count
    return s

def analyze_all():
    s1 = analyze_blocks(S1)
    s2 = analyze_blocks(S2)
    s3 = analyze_blocks(S3)
    return s1, s2, s3  # Возвращаем результаты из функции

def print_analyze(s1, s2, s3):
    print("S1:")
    for key, value in s1.items():
        print(f"{key}: {value}")
    print("-------------")
    print("S2:")
    for key, value in s2.items():
        print(f"{key}: {value}")
    print("-------------")
    print("S3:")
    for key, value in s3.items():
        print(f"{key}: {value}")

def new_ij(s1,s2,s3):
    ij1=set()
    ij2=set()
    ij3=set()
    for i in range(1,16):
        for j in range(1,8):
            if abs(1-s1[(i,j)]/8)>=5/8:
                ij1.add((i,j))
    for i in range(1,16):
        for j in range(1,8):
            if abs(1-s2[(i,j)]/8)>=1/2:
                ij2.add((i,j))
    for i in range(1,16):
        for j in range(1,4):
            if abs(1-s3[(i,j)]/8)>=5/8:
                ij3.add((i,j))
    return ij1,ij2,ij3

def analyze_ij(ij,num):
    X={}
    Y={}
    K={}
    if num!=1 and num!=2 and num!=3:
        print("Incorrect num of s blocks")
        return
    else:
        for ind in ij:
            x=ind[0]
            y=ind[1]
            x1=set()
            y1=set()
            buf1=set()
            buf2=set()
            #print("bin i:",bin(x))
            for i in range(0,4):
                if x&(1<<i):
                   x1.add(4-i)
            #print("num of bites in i ",x1)
            for i in x1:
                j=i+4*(num-1)
                buf2.add(j)
                buf1.add(P[j]+8)
            X[(x,y)]=buf1
            K[(x,y)]=buf2
            #print("final x: ",buf1)
            #print("final k: ",buf2)
            buf1=set()
            #print("bin j:",bin(y))
            if num==3:
                for i in range(0,2):
                    if y&(1<<i):
                       y1.add((2-i)+(num-1)*3)
            else:
                for i in range(0,3):
                    if y&(1<<i):
                       y1.add((3-i)+(num-1)*3)
            #print("num of bites in j ",y1)
            for i in IP:
                if IP[i] in y1:
                    buf1.add(i)
            #print("Y,X:",buf1)
            Y[(x,y)]=buf1
            X[(x,y)]|=buf1

    print("X: ",X)
    print("Y: ",Y)
    print("K: ",K)
    return X,Y,K
        #print(x1)
        #print(buf1)

def equation(aff1,aff2,aff3,inp,key,s1,s2,s3):
    ci=fiestel(inp,key)
    X,Y,K1=analyze_ij(aff1,1)
    s1_lin=s1
    s2_lin=s2
    s3_lin=s3
    edin=0
    nul=0
    #print(bin(inp))
    for key in X:
        count=0
        #print("--------------------")
        for i in X[key]:
            #print("i:",i)
            #print("i<<:",bin(1<<((15-i)+1)))
            if inp&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        for i in Y[key]:
            #print("i:",i)
            if ci&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        if count%2==0:
            s1_lin[key]+=1
        #else:
        #    s1_lin[key]=1
        #print(f"s1_lin[{key}]:{s1_lin[key]}")

    X,Y,K2=analyze_ij(aff2,2)
    for key in X:
        count=0
        #print("--------------------")
        for i in X[key]:
            #print("i:",i)
            #print("i<<:",bin(1<<((15-i)+1)))
            if inp&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        for i in Y[key]:
            #print("i:",i)
            if ci&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        if count%2==0:
            s2_lin[key]+=1
            
        #else:
        #    edin+=1
        #    s2_lin[key]=1
        #print(f"s2_lin[{key}]:{s2_lin[key]}")

    X,Y,K3=analyze_ij(aff3,3)
    for key in X:
        count=0
        #print("--------------------")
        for i in X[key]:
            #print("i:",i)
            #print("i<<:",bin(1<<((15-i)+1)))
            if inp&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        for i in Y[key]:
            #print("i:",i)
            if ci&(1<<((15-i)+1)):
                count+=1
        #print("--------------------")
        if count%2==0:
            s3_lin[key]+=1
        #else:
        #    s3_lin[key]=1
        #    edin+=1
        #print(f"s3_lin[{key}]:{s3_lin[key]}")
    return s1_lin,s2_lin,s3_lin,K1,K2,K3


    

        
        





# Вызываем функцию analyze_all() и передаем результаты в print_analyze()
s1_result, s2_result, s3_result = analyze_all()
print_analyze(s1_result, s2_result, s3_result)

print("------------------------------------------------------------------------------------")
aff1,aff2,aff3=new_ij(s1_result,s2_result,s3_result)
print(aff1)
print(aff2)
print(aff3)

s1={}
for i in aff1:
    if i not in s1:
        s1[i] = 0
s2={}
for i in aff2:
    if i not in s2:
        s2[i] = 0
s3={}
for i in aff3:
    if i not in s3:
        s3[i] = 0

for i in range(100):
    plaintext=randint(0,65535)
    s1,s2,s3,k1,k2,k3=equation(aff1,aff2,aff3,plaintext,2730,s1,s2,s3)
print("s1:",s1)
print("s2:",s2)
print("s3:",s3)

original_s1={}
for i in s1:
    if (s1[i]/100)>(1/2):
        if (s1_result[i]/16)>(1/2):
            original_s1[tuple(k1[i])]=0
        else:
            original_s1[tuple(k1[i])]=1
    elif (s1[i]/100)<(1/2):
        if (s1_result[i]/16)>(1/2):
            original_s1[tuple(k1[i])]=1
        else:
            original_s1[tuple(k1[i])]=0

original_s2={}
for i in s2:
    if (s2[i]/100)>(1/2):
        if (s2_result[i]/16)>(1/2):
            original_s2[tuple(k2[i])]=0
        else:
            original_s2[tuple(k2[i])]=1
    elif (s2[i]/100)<(1/2):
        if (s2_result[i]/16)>(1/2):
            original_s2[tuple(k2[i])]=1
        else:
            original_s2[tuple(k2[i])]=0

original_s3={}
for i in s3:
    if (s3[i]/100)>(1/2):
        if (s3_result[i]/16)>(1/2):
            original_s3[tuple(k3[i])]=0
        else:
            original_s3[tuple(k3[i])]=1
    elif (s3[i]/100)<(1/2):
        if (s3_result[i]/16)>(1/2):
            original_s3[tuple(k3[i])]=1
        else:
            original_s3[tuple(k3[i])]=0

print("original_s1:",original_s1)
print("original_s2:",original_s2)
print("original_s3:",original_s3)


