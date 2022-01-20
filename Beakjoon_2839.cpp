#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int N, dp[5003];

int main() {
    cin >> N;
    
    for (int i=3; i<=N; i++) {
        if (i == 3) {
            dp[i] = 1;
        }
        else if (i == 5) {
            dp[i] = 1;
        }
        else {
            if (dp[i-3]) {
                dp[i] = dp[i-3]+1;
            }
            if (dp[i-5]) {
                if (dp[i]) {
                    dp[i] = min(dp[i], dp[i-5]+1);
                }
                else {
                    dp[i] = dp[i-5] + 1;
                }
            }
        }
    }
    if (dp[N] == 0) {
        cout << -1 << endl;
    }
    else {
        cout << dp[N] << endl;
    }
}