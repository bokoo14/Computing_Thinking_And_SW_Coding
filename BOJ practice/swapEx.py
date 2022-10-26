# 참고: https://booknu.github.io/2019/04/24/%EC%9E%84%EC%8B%9C%EB%B3%80%EC%88%98%EC%97%86%EC%9D%B4swap/

# 더하기 뺴기만으로 swap
print("plus and minus swapping")
x=10
y=20
print(x, y)
x += y
y = x - y
x -= y
print("after swapping")
print(x, y)

# xor를 이용한 swap
print("xor swapping")
a= 100
b= 200
a ^= b
b ^= a
a ^= b
print("after swapping")
print(a, b)


# 곱하기, 나누기만으로 swap
print("mul and div swapping")
a=10
b=20
a *= b
b = a / b
a = a / b
print("after swapping")
print(a, b)
