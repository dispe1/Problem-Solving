# https://algospot.com/judge/problem/read/BRACKETS2

#스택을 이용해 짝이 맞지 않는 괄호 문제를 해결하는 알고리즘
def wellMatched(formula):
    #여는 괄호 문자들과 닫는 괄호 문자들
    opening = "({["
    closing = ")}]"
    #이미 열린 괄호들을 순서대로 담는 스택
    openStack = []
    for i in range(len(formula)):
        #여는 괄호인지 닫는 괄호인지 확인한다.
        if opening.find(formula[i]) != -1:
            #여는 괄호라면 무조건 스택에 집어넣는다.
            openStack.append(formula[i])
        else:
            #이외의 경우 스택 맨 위의 문자와 맞춰보자.
            #스택이 비어 있는 경우에는 실패
            if not openStack: return False
            #서로 짝이 맞지 않아도 실패
            if opening.find(openStack[-1]) != closing.find(formula[i]):
                return False
            #짝을 맞춘 괄호는 스택에서 뺀다.
            openStack.pop()
    #닫히지 않은 괄호가 없어야 성공
    return not openStack
