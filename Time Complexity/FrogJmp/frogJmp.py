def solution(X: int, Y: int, D: int) ->int:
    currentDistance = X
    numberJumps = 0
    while(currentDistance < Y):
        currentDistance += D
        numberJumps +=1
    return numberJumps

print(solution(10,85,30))