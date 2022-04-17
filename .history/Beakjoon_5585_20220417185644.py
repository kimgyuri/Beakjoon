pay = int(input())
coin = 1000-pay # 거스름 돈
count = 0

while coin != 0:
    if coin >= 500:
        count += (coin/500)
        coin %= 500
    elif coin >= 100:
        count += (coin/100)
        coin %= 100
    elif coin >= 50:
        count += (coin/50)
        coin %= 50
    elif coin >= 10:
        count += (coin/10)
        coin %= 10
    elif coin >= 1:
        count += (coin/1)
        coin %= 1

print(int(count))