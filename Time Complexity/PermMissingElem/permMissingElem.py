def solution(A: list) -> int:
    A.sort()
    for x in range(len(A)-1):
        if (A[x] + 1 != A[x+1]):
            return (A[x] + 1)

print(solution([2,3,1,5]))
print(solution([9,7,8,5]))