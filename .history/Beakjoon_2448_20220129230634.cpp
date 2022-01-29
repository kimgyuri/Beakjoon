#include <iostream>
#include <string>
using namespace std;

char arr[3072][6143];

void draw(int row, int col) {

    // 삼각형 첫번 째 줄
    arr[row][col] = '*';

    // 삼각형 두번 째 줄
    arr[row+1][col-1] = '*';
    arr[row+1][col+1] = '*';

    // 삼각형 세번 째 줄
    for (int i=0; i<5; i++) {
        arr[row+2][col-2+i] = '*';
    }
}

int main() {
    int N;
    cin >> N;

    // 배열 공백으로 선언
    for (int i=0; i<N; i++) {
        for (int j=0; j<2*N-1; j++) {
            arr[i][j] = ' ';
        }
    }

    
}