# runtime error

N = input()

arr = []

for i in range(N):
    num = input()
    arr.append(num)

    if(i == 0):
        print(num)
    elif(i%2 != 0):
        arr.sort()
        print(arr[len(arr)/2-1])
    else: 
        arr.sort()
        print(arr[len(arr)/2])