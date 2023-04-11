def solution(s):
    center=len(s)//2 # 가운데 글자 뽑기
    if len(s)%2 != 0:  # 홀수일때
        return s[center]
    else: # 짝수 일때
        return s[center-1:center+1] 
