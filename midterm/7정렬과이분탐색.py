import random
SEED, MIN, MAX, N = 2022, 1, 100000, 10000
random.seed(SEED)
S = random.sample(range(MIN, MAX), N)

# 7-1
S.sort(key = lambda x: (-len(str(x)), x))

print(S[100])

# 7-2
S.sort()
def sol(find, first, last):
    if first>last:
        return 
    mid = (first+last)//2

    if mid == find:
        return find

    if find < mid: # 찾는 값이 더 작으면
 
        return sol(first, mid-1)
    else:
        print(mid, "UP")
        return sol(mid+1, last)


