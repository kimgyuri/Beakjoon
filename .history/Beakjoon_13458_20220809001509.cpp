#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N; // 시험장 개수
int B, C; // 총 감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수

int arr[1000001];

int main() {
    cin >> N;
    
    for(int i=0; i<10; i++){
        int A; // 시험장에 있는 응시자의 수
        cin >> A;
        arr[A]++;
    }
    cin >> B >> C;

    int result = 0;
    int main = 0; // 총 감독관 수
    int sub = 0; // 부 감독관 수
    for(int i=0; i<sizeof arr; i++){
        if (arr[i] == 0) continue; // 해당 요소가 0이면 무시
        main = i-B;
        if (main > 0) {
            if (main%C != 0) sub++; // 나머지가 있을 떄 부 감독관 수를 1명 더 늘려줘야 됨
            sub += main/C;
        }
        result += (main+sub) * arr[i];
    }
    cout << result;

    return 0;
}