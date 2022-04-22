# N = int(input())

# num = 9
# alphabet = []
# dic = {}

# for _ in range(N):
#     alphabet.append(str(input())) # alphabet에 단어 넣어주기

# alphabet.sort(key = lambda x: len(x), reverse=True) # 길이가 긴 것부터 정렬
# calc = list(list(0 for j in range(len(alphabet[0]))) for i in range(N)) # 단어 중 가장 긴 길이만큼의 크기를 가진 리스트 생성

# for i in range(N):
#     for j in range(len(alphabet[i])):
#         calc[i][j] = alphabet[i][-(j+1)] # 리스트에 알파벳 하나씩 채워 넣기 (반대로)

# for i in range(len(calc[0])-1, -1, -1):
#     for j in range(N):
#         if (calc[j][i] != 0) and (calc[j][i] not in dic): # 딕셔너리에 알파벳이 없으면 넣기
#             dic[calc[j][i]] = num
#             num -= 1

# result = 0
# string = ""
# for i in range(N): 
#     for j in alphabet[i]:
#         string += str(dic[j]) # 단어를 딕셔너리에 있는 숫자들로 바꿈
#     result += int(string)
#     string = ""

# print(result) 

N = int(input())

alphabet = []
dic = {}
num_list = []

for i in range(N):
    alphabet.append(str(input(i)))

for i in range(N):
    for j in range(len(alphabet[i])):
        if alphabet[i][j] not in dic:
            dic[alphabet[i][j]] = 10 ** (len(alphabet[i])-j-1) # 딕셔너리에 알파벳이 존재하지 않으면 해당 자리수에 맞게 숫자로 바꾸어 삽입 (10의 자리면 10)
        else:
            dic[alphabet[i][j]] += 10 ** (len(alphabet[i])-j-1) # 딕셔너리에 알파벳이 존재하면 존재하는 숫자에 자리에 맞게 더함

for value in dic.values():
    num_list.append(value)

num_list.sort(reverse=True)

result = 0
num = 9

for i in num_list:
    result += num * i
    num -= 1

print(result)