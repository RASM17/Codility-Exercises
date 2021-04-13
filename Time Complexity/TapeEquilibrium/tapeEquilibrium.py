def solution(A: list) -> int:
    minDict = {}
    for p in range(1,len(A)-1):
        firstHalf = A[:p]
        secondHalf = A[p:]
        minDict[p]=min(sum(firstHalf), sum(secondHalf))
    return min(minDict, key=minDict.get)

print(solution([3,1,2,4,3]))