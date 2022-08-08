#include <iostream>
#include <vector>
using namespace std;

int N; // 시험장 개수
int B, C; // 총 감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수

vector<int> vec;

int main() {
    cin >> N;
    
    for(int i=0; i<N; i++){
        int A; // 시험장에 있는 응시자의 수
        cin >> A;
        vec.push_back(A);
    }
    return 0;
}