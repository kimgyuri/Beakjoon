#include <iostream>
#include <string>
using namespace std;

void star(int i, int j, int N) {
    if ((i%3 == 1) && (j%3 == 1)) {
        cout << " ";
    } else {
        if (N/3 == 0){
            cout << "*";
        } else {
            star(i, j, N/3);
        }
        
    }
}

int main() {
    int N;

    cin >> N;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            star(i, j, N);
        }
        cout << '\n';
    }
}