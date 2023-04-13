n=5
#2진수 함수 사용해서 문제풀기
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
brr1=[]
brr2=[]
a[2:] # 진수로 변환하고 n개로 뽑기
for i in arr:
    a=bin(i)
    b=a[2:]
    if len(b)<n:
        b="0"*(n-len(b))+b # 앞에다가 0붙이기 해야함 
        b=b.replace('1','#').replace('0'," ")
        brr1.append(b)
    else:
        b=b.replace('1','#').replace('0'," ")
        brr1.append(b)
for i in arr2:
    a=bin(i)
    b=a[2:]
    if len(b)<n:
        b="0"*(n-len(b))+b # 앞에다가 0붙이기 해야함 
        b=b.replace('1','#').replace('0'," ")
    
        brr2.append(b)
    else:
        b=b.replace('1','#').replace('0'," ")
        brr2.append(b)    
print(brr1)
print(brr2)
# 값 비교 
# zip()함수를 이용해서 하기
