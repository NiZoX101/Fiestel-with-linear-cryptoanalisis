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
E={
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

P={
    1:8,
    2:7,
    3:3,
    4:2,
    5:5,
    6:4,
    7:1,
    8:6
    }


def expansion_per(text):
    #x1=set()
    permut=set()
    #for i in range(0,8):
    #            if text&(1<<i):
    #               x1.add(8-i)
    for p in E:
        if E[p] in text:
            permut.add(p)
    #print("permutation: ",permut)
    return permut

def xor(text,key):
    key1=set()
    xor=set()
    for i in range(0,12):
                if key&(1<<i):
                   key1.add(12-i)
    #print("key: ",key1)
    xor=key1^text
    #print("Xor: ",xor)
    return xor

def analyze_s(text):
    s1=0
    for i in range(1,5):
        #print("i:",i)
        if i in text:
            s1+=1<<(4-i)
    s1=S1[s1]
    #print("s1:",bin(s1))

    s2=0
    for i in range(1,5):
        #print("i:",i+4)
        if i+4 in text:
            s2+=1<<(4-i)
    s2=S2[s2]
    #print("s2:",bin(s2))

    s3=0
    for i in range(1,5):
        #print("i:",i+8)
        if i+8 in text:
            s3+=1<<(4-i)
    s3=S3[s3]
    #print("s3:",bin(s3))

    s=set()

    for i in range(0,4):
        if s1&1<<i:
            s.add(3-i)
    #print(s)

    for i in range(0,4):
        if s2&(1<<i):
            s.add(6-i)
    #print(s)

    for i in range(0,3):
        if s3&(1<<i):
            s.add(8-i)
    #print(s)
    return s

def final_permutation(text):
    permut=set()
    for p in P:
        if P[p] in text:
            permut.add(p)
    #print("permutation: ",permut)
    return permut

def fiestel(text,key):
    L=set()
    R=set()
    for i in range(0,16):
        if text&(1<<i):
            if 16-i<=8:
                L.add(16-i)
            else:
                R.add(16-i-8)
    #print("L: ",L)
    #print("R: ",R)
    R1=R
    exp=expansion_per(R)
    L1=L^final_permutation(analyze_s(xor(exp,key)))
    #print("L1: ",L1)
    #print("R1: ",R1)
    cipher=output_f(L1,R1)
    return cipher



def output_f(text1,text2):
    cipher=0
    for i in text2:
        cipher+= 1<<(8-i)
        #print("text2 ",bin(cipher))
    for i in text1:
        cipher+= 1<<(8-i+8)
        #print("text1 ",bin(cipher))
    #print(bin(cipher)[2:])
    return cipher

#key="101010101010"
#key=int(key,2)

#binary_number1 = '0000000000001001'  # ѕример двоичного числа
## ѕреобразование двоичного числа в дес€тичное число
#decimal_number1 = int(binary_number1, 2)
#print(binary_number1)
#fiestel(decimal_number1,key)

