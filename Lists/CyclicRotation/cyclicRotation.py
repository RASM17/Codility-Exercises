def solution(A: list, K:int) -> list:
    for i in range(K):
        last = A.pop()
        A = [last] + A
    return A

print(solution ([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0],1))
print(solution([1, 2, 3, 4],4))