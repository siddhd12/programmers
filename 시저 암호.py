def solution(s, n):
    a=list(s) # 값 list 로 만들기 
    t="abcdefghijklmnopqrstuvwxyz" #소
    e="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #대
    re=[]
    for i in a:  # 리스트 안에 값 뽑기 [a,b,c]
        if i.isupper():  # 대문자 확인
                re.append(e[e.index(i)+n-26]) # 대문자 암호화
        elif i==" ": #  공백 넣기
                re.append(i)
        else: # 소문자 확인
                re.append(t[t.index(i)+n-26]) # 소문자 암호화
    return "".join(re)
  
 #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 첫 시도 시 한거
q='a b c'
t="abcdefghijklmnopqrstuvwxyz" #소
e="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #대
n=5
re=[] # 마지막 리스트
c=list(q) # 받은 값 리스트
# print(c)
# print(len(c))
# print(a.index(c[0+n]))
# print(a[0+n])
print("n의 값", n)
print(c)
for i in c:  # 리스트 안에 값 뽑기 [a,b,c]
    if i.isupper():  # i가 대문자라면
        print('이전',i,e.index(i))    # 받은값 , t에서의 인덱스
        print('인덱스 번호 바뀐거',i,e.index(i)+n)   # 받은 값,  암호자리(t에서의 인덱스 + n)
        print('바꿀 값',e[e.index(i)+n-26])   # 소문자 암호 자리 뽑기
        re.append(e[e.index(i)+n-26]) # 리스트에 값 넣기
    else:    
        print('이전',i,t.index(i))    # 받은값 , t에서의 인덱스
        print('인덱스 번호 바뀐거',i,t.index(i)+n)   # 받은 값,  암호자리(t에서의 인덱스 + n)
        print('바꿀값',t[t.index(i)+n-26])   # 소문자 암호 자리 뽑기
        re.append(t[t.index(i)+n-26]) # 리스트에 값 넣기
print('바뀐값:',re)
# print(len(t))
#     0 ,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,17,18.19,20,21,22,23,24,25
#  -26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1 

# z의 경우를 포함하기위해 한 것
# c= 'abc'
#  0, 1, 2
# a+1(1-26) -25   # b
# b+1(2-26) -24   # c
# c+1(3-26) -23   # d
# z+1(26-26)      # a

# b=1
# b-26= -25
 
#        26
# 마지막 공백을 생각도 못했어서 40분동안 헤맸다. 문제 무조건 
