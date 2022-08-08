T = int(input())

for _ in range(T):
    N = int(input())
    stock = list(map(int, input().split()))

    total = 0
    
    while len(stock) > 0:

        tmp = stock.pop()

        for i in range(len(stock)-1, -1, -1):
            if tmp >= stock[i]:
                total += (tmp-stock[i])
                stock.pop()
            else:
                break
    
    print(total)

# from collections import deque

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     stock = deque(list(map(int, input().split())))

#     benefit = []
#     stock_max = max(stock)
#     total = 0

#     while len(stock) > 0:
#         tmp = stock.popleft()
#         if tmp < stock_max:
#             benefit.append(tmp)
#         elif tmp == stock_max and len(benefit) > 0:
#             while len(benefit) > 0:
#                 total += (tmp-benefit.pop())
#         if len(stock) > 0:
#             stock_min = min(stock)
#             stock_max = max(stock)
#     print(total)

