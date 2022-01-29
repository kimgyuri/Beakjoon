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
        else if (i == 4) {
            dp[i] = 0;
        }
        else if (i == 5) {
            dp[i] = 1;
        }
        else {
            if(dp[i-3] != 0) {
                dp[i] = min(dp[i-3]+1, dp[i-5]+1);
            }
        }
    }
}