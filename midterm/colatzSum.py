import sys

input = sys.stdin.readline

# 콜라츠 수열 1억~2억 사이의 값 중 콜라츠 수열의 길이가 가장 긴 수열을 구하시오-> 재귀는 안됨

def collatz(n):
  if n == 1:
    return [1]
  elif n % 2 == 0:
    return [n] + collatz(n // 2)
  else:
    return [n] + collatz(3 * n + 1)

'''
def collatz(n):
  seq = [n]  # 수 들을 담을 리스트

  while n > 1:
    if n % 2 == 0:  # n이 짝수일때
      n = n // 2
    else:  # n이 홀수일때
      n = 3 * n + 1

    seq.append(n)

  return seq  # 콜라츠의 수열


answer = []
print(collatz(123))
print(max(collatz(123)))
for i in range(123, 321):
  length = len(collatz(i))
  answer.append(length)

# print(answer)
mm = max(answer)
print(mm)
'''
'''
res_seq = []
for i in range(12345,54322):
    res_seq.append(len(collatz(i)))

print(res_seq.index(max(res_seq)) + 1)
print(max(res_seq))
'''
maximum = 0 # 계산 횟수를 저장할 변수
result = 0  # 최대 계산 횟수일 경우 어떤 수에서 발생했는지 저장하는 변수

for i in range(123, 322):
    counter = 1 # 카운터는 매번 반복문이 다시 실행될 때 초기화 되어야 한다.

    j = i # i각 계속 연산되어야 하므로 따로 변수 j를 주어 i는 보존
    while True:
        if j == 1: # 계산 결과가 1이 되면 다음 숫자로 넘어가야 해서 while문 종료
            if maximum < counter: # 최댓값일 때 변수에 기록
                maximum = counter
                result = i

            break # while 문 종료

        counter += 1

        if j % 2 == 0:
            j = j / 2
        else:
            j = 3 * j + 1


print(result, maximum)  # 525회 계산을 하는 837799
