def solution(N: int) -> int:
    #Convert to binary
    nListBin = list(f'{N:01b}')
    #print(nListBin)
    currentGap = 0
    longestGap = 0
    for x in nListBin:
        if x == '0':
            currentGap +=1
        else:
            if (currentGap > longestGap):
                longestGap = currentGap
                currentGap = 0
    return longestGap

print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
print(solution(32))