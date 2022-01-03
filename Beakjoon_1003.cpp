#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T, N;
int dp[41];

int fibonacci(int n) {
    if (n == 0) {
        dp[n] = 0;
        return dp[n] = 0;
    } else if (n == 1) {
        dp[n] = 1;
        return dp[n] = 1;
    } else {
        if (dp[n] != 0) {
            return dp[n];
        }
        else {
            return dp[n] = fibonacci(n-1) + fibonacci(n-2);
        }
    }
}

int main() {
    cin >> T;

    for(int i=0; i<T; i++) {
        cin >> N;
        if(N == 0) {
            cout << 1 << " " << 0 << endl;
        }
        else if(N == 1) {
            cout << 0 << " " << 1 << endl;
        }
        else {
            fibonacci(N);
            cout << dp[N-1] << " " << dp[N] << endl;
        }
    }
    
}