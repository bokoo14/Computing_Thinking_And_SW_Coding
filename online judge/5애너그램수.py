import sys
input = sys.stdin.readline

# 애너그램: 알파벳이 나열된 순서는 다르지만, 알파벳의 구성이 일치하는 문자열
n=int(input())
array = list(map(int,input().split()))

answer=0
for i in range(0, len(array)):
    array[i]=list(str(array[i]))
    array[i].sort(key= lambda x: int(x))
    #print(array[i])
    if list(str(n))==array[i]:
        answer+=1

print(answer)

'''
n=input().strip()
array = list(map(str,input().split()))

answer=0
for i in range(0, len(array)):
    array[i]=list(str(array[i]))
    array[i].sort(key= lambda x: ord(x))
    n=list(n)
    n.sort(key= lambda x: ord(x))
    print(array[i])
    print(list(n))
    if n==array[i]:
        answer+=1

# 에너그램의 수가 모두 몇개인지 출력
print(answer)
'''