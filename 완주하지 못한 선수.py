def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!= completion[i]: # 1. 안에 있을때 경우
            return participant[i]
    return participant[-1]  # 2. completion이 아예 아무도 없을 경우(["a"],[])
# return participant[0] 이 안되는 이유 ['a','b'] ,[a] 인경우 for문에서 [a]만 확인하고
# 벗어나서 return participant[0] 이 리턴이되는데 participant[0]은 'a' 이기 때문에 [-1]로 해야한다
