from random import *

n = int(input('data size :'))               #데이터 크기 설정
p = 1                                       #패리티 비트 크기 설정
while(2**p < n + p + 1):                    #ilovepython, 크거나같음은 작음의 반대
    p += 1
print('p :', p)
val = 0
length = 0                                  #index 이진수 길이

list1 = [1,0,0,1,0,1,0]                                  #0부터 10까지의 랜덤 수열 생성

"""
for i in range(n):
    list1.append(randint(0, 1))
"""

print('original data :', list1)
for i in range(p):
    list1.insert(2**i - 1, 0)               #parity 0으로 채워넣음
print('parity init :', list1)               #리스트 출력

#parity check
for i in range(p):
    x = 2**(p-1)
    val = 0
    while x < n+p:
        for j in range(2**(p-1)):
            if j+x > n+p:
                if val % 2 == 1:
                    list1[2**i] = 1 - list1[2**i]   #parity 바꿔줌
                break                       #여기서 break 해줘도 x+=2**p에서 x는 n+p 넘어감
            val += list1[j + x - 1]
        x += 2**p

print('send', list1)

print(' ')
error = randint(0, p-1)
print('error occured :', error)
list1[error] = 1 - list1[error]             #0 1 바꿔줌
print('list1 :', list1)

#오류 검출
val = 0
syndrome = []
for i in range(p):
    for j in range(n+p):
        index = bin(j+1)                    #이진수 변환
        index = index[2:]                   #앞에 0b 잘라줌
        index = list(index)                 #*주의, 리스트로 만들어줘도 형식은 여전히 str임
        length = len(index)
        for j in range(p - length):         #길이 정규화, p까지의 길이까지 앞에 0을 붙여줌
            index.insert(0, '0')
        #print(index)
        if index[-(i+1)] == '1':            #Pn의 범위는 인덱스의 이진수의 n번째수가 1인 것의 집합 
            val += list1[j]
    val = val % 2
    print(i, val)
    syndrome.append(val)

print('syndrome', syndrome)
