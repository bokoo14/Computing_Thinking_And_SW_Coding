import sys

# 5-1
F = [0]*1001
F[1]=1
F[2]=2
F[3]=3

n= 30
for i in range(4, n+1):
    F[i]= F[i-1]+2*F[i-2]-F[i-3]

print(F[30])

# 5-2
F = [0]*1001
F[1]=1
F[2]=2
F[3]=3

n= 1000
for i in range(4, n+1):
    F[i]= F[i-1]+2*F[i-2]-F[i-3]

print(str(F[1000])[:5])

# 5-3
F = [0]*1001
F[1]=1
F[2]=2
F[3]=3

n= 1000
for i in range(4, n+1):
    F[i]= F[i-1]+2*F[i-2]-F[i-3]
