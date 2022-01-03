// DP
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T, n;
int dp[11];

int func(int n) {
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    
    if (dp[n] != 0) {
        return dp[n];
    }
    else {
        return dp[n] = func(n-1) + func(n-2) + func(n-3);
    }
}

int main() {
    cin >> T;

    for (int i=0; i<T; i++) {
        cin >> n;
        
        func(n);
        cout << dp[n] << endl;
    }
}