# from collections import deque
# words = deque(list(map(str, input().split())))

# result = ""

# while len(words) != 0:
#     word = words.popleft()
#     if len(result) == 0 :
#         if 'U' in word:
#             result += 'U'
#     elif len(result) == 1:
#         if 'C' in word:
#             result += 'C'
#     elif len(result) == 2:
#         if 'P' in word:
#             result += 'P'
#     elif len(result) == 3:
#         if 'C' in word:
#             result += 'C'

# if result == 'UCPC':
#     print('I love UCPC')
# else:
#     print('I hate UCPC')

def ucpc(words):
    check_alpha = ['U', 'C', 'P', 'C']

    result = 'I love UCPC'

    for alpha in check_alpha:
        if alpha in words:
            alpha_index = words.index(alpha)
            words = words[alpha_index+1:]
        else:
            result = 'I hate UCPC'
            break
    return result

if __name__ == '__main__':
    words = input()
    print(ucpc(words))
