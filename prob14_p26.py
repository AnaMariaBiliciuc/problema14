n=int(input('Introduceti numarul de linii: '))
x=[]
if (n>=2) and (n<=10) :
    for i in range(0,n):
        y=[]
        for j in range(0,n):
            y.append(int(input('Introduceti elementele matricelui: ')))
            x.append(y)
    print('Matricele: ',x)
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
for i in range(len(x)):
    for j in range(len(x[0])):
        if (i==j):
            s1.append(x[i][j])
        if ((i+j)==(n-1)):
            s2.append(x[i][j])
        if (i<j):
            s3.append(x[i][j])
        if (i>j):
            s4.append(x[i][j])
        if  ((i+j)<(n-i)):
            s5.append(x[i][j])
        if ((i+j)>(n-1)):
            s6.append(x[i][j])
print('Suma elementelor de pe diagonala principala: ',sum(s1))
print('Suma elementelor de pe diagonala secundara: ',sum(s2))
print('Suma elementelor mai sus de diagonala principala: ',sum(s3))
print('Suma elementelor mai jos de diagonala principala: ',sum(s4))
print('Suma elementelor mai sus de diagonala secundara: ',sum(s5))
print('Suma elementelor mai jos de diagonala secundara: ',sum(s6))