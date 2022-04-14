def solution(n):
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
                answer == (-1)
    return int(answer)


def main():
    print(solution(18))
    print(solution(4))
    print(solution(6))
    print(solution(9))
    print(solution(11))

if __name__ == "__main__":
    main()