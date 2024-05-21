from coding import *
permut={
    1:7,
    2:5,
    3:3,
    4:6,
    5:4,
    6:8,
    7:2,
    8:1,
    9:8,
    10:3,
    11:1,
    12:5
    }

#IP_1={
#    1:7,
#    2:4,
#    3:3,
#    4:6,
#    5:5,
#    6:8,
#    7:2,
#    8:1
#    }

delta_a={}
for num in range(1,16):
    delta_a[num]=set()
def gen_a():
    for num in range(1,16):
        for i in range(0,16):
            for j in range(0,16):
                if i^j == num:
                    delta_a[num].add((i,j))
                    print(f"{bin(num)}: {bin(i)}  {bin(j)}")
    print("---------------------------------------------------------")

def dependence_ac(s):
    print("S-block:")
    delta_c={}
    if s!=S3:
        for num in range(1,16):
            for num1 in range(0,8):
                delta_c[(num,num1)]=0
    else:
        for num in range(1,16):
            for num1 in range(0,4):
                delta_c[(num,num1)]=0
    for num, pairs in delta_a.items():
        for k in pairs:
            sum1 = s[k[0]] ^ s[k[1]]
            print(f"{bin(sum1)}={bin(s[k[0]])}^{bin(s[k[1]])}          k[0]={k[0]} k1={k[1]}    num={num} sum1={sum1}")
            delta_c[(num, sum1)] += 1
    print (delta_c)
    print("---------------------------------------------------------")
    return delta_c

def optimal():
    max=0
    opt1={}
    opt2={}
    opt3={}
    for pairs,nums in ac1.items():
        if nums>max:
            max=nums
    for pairs,nums in ac1.items():
        if nums == max:
            opt1[pairs]=nums
    max=0
    for pairs,nums in ac2.items():
            if nums>max:
                max=nums
    for pairs,nums in ac2.items():
        if nums == max:
            opt2[pairs]=nums
    max=0
    for pairs,nums in ac3.items():
            if nums>max:
                max=nums
    for pairs,nums in ac3.items():
        if nums == max:
            opt3[pairs]=nums
    print(opt1)
    print(opt2)
    print(opt3)
    return opt1,opt2,opt3

def optimal1():
    for op1 in optim1.keys():
        for op2 in optim2.keys():
            for op3 in optim3.keys():
                C=0
                A=0
                A+=(op1[0]<<8)
                A+=(op2[0]<<4)
                A+=op3[0]
                flag=0
                for key,value in permut.items():
                    for key1,value1 in permut.items():
                        print(f"{bin(A)}")
                        flag=0
                        print(f"{key}:{value}   {key1}:{value1}    {((1<<(12-key))&A)>>(12-key)} {((1<<(12-key1))&A)>>(12-key1)}   ")
                        if value==value1:
                            print(f"{key}=?{key1}")
                            if ((1<<(12-key))&A)>>(12-key)!=((1<<(12-key1))&A)>>(12-key1):
                                print("---------------------------------------------------------------------------")
                                flag=1
                                break
                    if flag==1:
                        break
                if flag!=1:
                    C+=op1[1]<<5
                    C+=op2[1]<<2
                    C+=op3[1]
                    print("A:",bin(A))
                    print("C:",bin(C))
                    return A,C
    print("Something wrong")
    return

def open_pairs(A,C):
    x_x1=set()
    for x in range(0,256):
        for x1 in range(0,256):
            ex=0
            ex1=0
            for key,value in permut.items():
                if (1<<(8-value))&x:
                    ex+=1<<(12-key)
                if (1<<(8-value))&x1:
                    ex1+=1<<(12-key)
            if ex^ex1==A:
                y=fiestel(x,2730)>>8
                y1=fiestel(x1,2730)>>8
                print(f"y:{bin(y)}  y1:{bin(y1)}")
                sx=0
                sx1=0
                for key,value in P.items():
                    if (1<<(8-key))&y:
                        sx+=1<<(8-value)
                    if (1<<(8-key))&y1:
                        sx1+=1<<(8-value)
                print(f"sx:{bin(sx)}  sx1:{bin(sx1)}")
                if sx^sx1==C:
                    x_x1.add((x,x1,y,y1,ex,ex1,sx,sx1))
                    print(f"x: {bin(x)}  y: {bin(y)}  ex: {bin(ex)}  sx: {bin(sx)}")
                    print(f"x1: {bin(x1)}  y1: {bin(y1)}  ex1: {bin(ex1)}  sx1: {bin(sx1)}")
    return x_x1





gen_a()
print(delta_a)
print("------------------------------------")
ac1=dependence_ac(S1)
ac2=dependence_ac(S2)
ac3=dependence_ac(S3)

print ("ac1:",ac1)
print("--------------")
print ("ac2:",ac2)
print("--------------")
print ("ac3:",ac3)

print("------------------------------------")
optim1,optim2,optim3=optimal()
A,C=optimal1()
print("-------------------------------------")
x_x1=open_pairs(A,C)
print("A:",bin(A))
print("C:",bin(C))
print(x_x1)

#print("S1:")
#for key,value in S1.items():
#    print(f"{bin(key)}: {bin(value)}")

#print("S2:")
#for key,value in S2.items():
#    print(f"{bin(key)}: {bin(value)}")

#print("S3:")
#for key,value in S3.items():
#    print(f"{bin(key)}: {bin(value)}")


