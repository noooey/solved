from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    answer = 0
    for _ in range((len(queue1) + 1) * 2):
        if sum1 == sum2:
            return answer
        elif sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            answer += 1
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
            answer += 1
    if sum1 != sum2:
        return -1
    return answer
