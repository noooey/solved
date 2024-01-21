from itertools import product

def solution(users, emoticons):
    rates = [10, 20, 30, 40]   # 할인율

    total = []
    for rate_com in product(rates, repeat=len(emoticons)):
        join, sale = 0, 0
        for user in users:
            isUser = False
            tmp_sale = 0
            thres_rate = user[0]
            thres_cost = user[1]
            for i in range(len(rate_com)):
                if rate_com[i] >= thres_rate:
                    tmp_sale += emoticons[i] * (100 - rate_com[i]) * 0.01
                if tmp_sale >= thres_cost:
                    join += 1
                    isUser= True
                    break
            if not isUser:
                sale += tmp_sale
        total.append([join, sale])

    total = sorted(total, key=lambda x: (x[0], x[1]), reverse=True)

    return total[0]   # 가입 수, 매출액
