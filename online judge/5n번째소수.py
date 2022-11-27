import sys
input = sys.stdin.readline

# 소수인지 판별
def is_prime(k):
    if k<2:
        return False
    else:
        for c in range(2, int(k**(0.5))+1):
            if k%c==0: # 나누어지는 값이 있으면 약수가 있음 = 소수가 아님
                return False
    return True

n = int(input()) 
answer=0 # 몇번째 소수인지 
cnt=0 # 숫자 올려주기
while 1:
    if answer==n: #n번째 소수라면
        print(cnt)
        break
    cnt+=1
    if is_prime(cnt): # 소수라면 1씩 올려줌
        answer+=1 
    
