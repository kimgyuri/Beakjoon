#include <iostream>
#include <string>
using namespace std;

char arr[2187][2187];

void draw(int N) {
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++)  {
            if ((i%3 == 0) || (j%3 == 0)) {
                arr[i][j] = ' ';
            }
            else {
                arr[i][j] = '*';
            }
        }
    }
}
int main() {
    int N;
    cin >> N;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cout << arr[i][j];
        }
        cout << endl;
    }
}