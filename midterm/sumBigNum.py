import sys
input = sys.stdin.readline
# 10억~11억까지 합을 구하시오->for로는 못구함. 자연수의 합공식(오일러의 공식)으로 풀어야 함
# 10억~20억 합
def sum_gauss(n):
	return int(n*(n+1)/2)

a=sum_gauss(2**30)
print(a)

b=sum_gauss(2**40)
print(b)

print(b-a)
