def solution(n):
    n = int(input)
    answer = 0
    if n%5 == 0:
        answer = n/5
    else:
        while n>0:
            n -= 3
            answer += 1
            if n%5 == 0:
                answer += n/5
                break
            elif n == 1 or n == 2:
                answer = -1
                break
    return int(answer)


def main():
    solution()

if __name__ == "__main__":
    main()