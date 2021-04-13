def solution(X: int, A: list) -> int:
    leafList = [None] * X
    for index, i in enumerate(A):
        # (i-1) since postion 0 of river is land so no leaf is needed
        if(i <= X and leafList[i-1] is None):
            leafList[i-1] = index
    return -1 if None in leafList else max(leafList)

print(solution(5, [1,3,1,4,2,3,5,4]))