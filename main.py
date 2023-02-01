import sys
  
n = int(input())
target = [] 
result = [] # 순열구조일 경우 : pop, push 구별
stack = []

for i in range(n) :
    target.append(int(sys.stdin.readline()))

# 숫자 증가
for i in range(1, n+1) :
    stack.append(i)
    result.append("+")

    if i == target[0] :
        target.remove(i)
        stack.remove(i)
        result.append("-")
        if len(stack) != 0 or len(target) != 0 :
            while True :
                if len(stack) == 0 or len(target) == 0 :
                    break
                if target[0] == stack[-1] :
                    target.remove(target[0])
                    stack.remove(stack[-1])
                    result.append("-")
                else :
                    break

if len(stack) == 0  and len(target) == 0 :
    for i in result :
        print(i)
else : print("NO")
            
