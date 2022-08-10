#include <iostream>
#include <algorithm>
#define MAX_T 7
#define MAX_P 1002 
using namespace std;

int N; // 남은 일 수
int T[MAX_T]; // 상담을 완료하는데 걸리는 기간
int P[MAX_P]; // 상담 시 받을 수 있는 금액
int DP[MAX_P];

int main() {

    cin >> N;

    // 1. 배열 초기화
    for ( int i = 0; i < N; i++ ) {
        cin >> T[i] >> P[i];
    }

    // 2. DP 계산
    // 원래의 DP라면 0번째 부터 계산하지만 이 문제의 경우 뒤에서부터 계산하는 것이 더 쉽다.
    // 퇴사일을 넘기는 경우를 바로 배제할 수 있기 때문!
    for ( int i = N; i >= 0; i--) {
        // 상담 완료 일 수가 퇴사날을 넘을 때
        if ( i + T[i] > N + 1 ) { 
            DP[i] = DP[i+1]; 
        }
        // 이전 상담의 최대 금액 + 현재 얻을 수 있는 금액 vs 전날의 최대 금액
        DP[i] = max(DP[i+T[i]] + P[i], DP[i+1]);
    }

    cout << DP[0];

    return 0;
}

// 참고 : https://yabmoons.tistory.com/1