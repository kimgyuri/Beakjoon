#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N; // 시험장 개수
int B, C; // 총 감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수

int DAT[1000001]; // index: 응시자 수, value: 응시자 수 카운팅

int main() {
    cin >> N;
    
    for(int i=0; i<N; i++){
        int A; // 응시자의 수
        cin >> A;
        DAT[A]++; 
    }
    cin >> B >> C;

    int result = 0;
    for(int i=1; i<sizeof DAT; i++){
        if (DAT[i] == 0) continue; // 해당 요소가 0이면 무시

        int sub = 0; // 부 감독관 수
        int temp = i-B; // 응시자수 - 총 감독관이 감시할 수 있는 응시자 수
        if (temp > 0) {
            if (temp%C > 0) sub++; // 나머지가 있을 떄 부 감독관 수를 1명 더 늘려줘야 됨
            sub += temp/C;
        }

        result += (1+sub) * DAT[i]; // (총 감독관 수 + 부 감독관 수) * 
    }
    cout << result;

    return 0;
}