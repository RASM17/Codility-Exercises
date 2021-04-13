def checkPairs(left: chr, right: chr) -> bool:
    if left == '{' and right == '}':
        return True   
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True 
    return False

def solution(S: str) -> int:
    leftSymbols = []
    for symbol in S:
        if (symbol == '{' or symbol == '(' or symbol == '[' ):
            leftSymbols.append(symbol)
        else:
            if (len(leftSymbols) == 0 or (not checkPairs(leftSymbols.pop(), symbol))):
                return 0
    if len(leftSymbols) != 0:
        return 0
    return 1

print(solution("{[()()]}"))
print(solution("{[()()]"))
print(solution("{()()}"))