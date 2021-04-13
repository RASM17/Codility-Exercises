def solution(A: list) -> list:
    oddList = []
    for x in A:
        if(not (x in oddList)):
            count = A.count(x)
            if (count % 2 != 0):
                oddList.append(x)
            
    return oddList

print(solution([9,3,9,3,9,7,9]))