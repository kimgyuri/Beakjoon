#include <iostream>
#include <string>
using namespace std;

char arr[3072][6143];

void draw(int row, int col) {

    // 삼각형 첫 번째 줄
    arr[row][col] = '*';

    // 삼각형 두 번째 줄
    arr[row+1][col-1] = '*';
    arr[row+1][col+1] = '*';

    // 삼각형 세 번째 줄
    for (int i=0; i<5; i++) {
        arr[row+2][col-2+i] = '*';
    }
}

void triangle(int len, int row, int col) {
    if (len == 3) {
        draw(row, col);
        return;
    }

    triangle(len/2, row, col); // 첫 번째 삼각형의 꼭짓점
    triangle(len/2, row+len/2, col-len/2); // 두 번째 삼각형의 꼭짓점
    triangle(len/2, row+len/2, col+len/2);
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

    triangle(N, 0, N-1); // 가장 큰 삼각형부터

    for (int i=0; i<N; i++) {
        for (int j=0; j<2*N-1; j++) {
            cout << arr[i][j];
        }
        cout << endl;
    }

    
}