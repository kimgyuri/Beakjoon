#include <iostream>
#include <string>
using namespace std;

char arr[3072][6143];

void draw(int row, int col) {
    
}

int main() {
    int N;
    cin >> N;

    // 배열 공백으로 선언
    for (int i=0; i<N; i++){
        for (int j=0; j<2*N-1; j++){
            arr[i][j] = ' ';
        }
    }

    
}