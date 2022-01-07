#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n, num;

int main() {
    cin >> n;

    int wine[n+1], dp[10002];

    for (int i=1; i<=n; i++) {
        cin >> num;
        wine[i] = num;
    }

    dp[1] = wine[1];
    dp[2] = dp[1] + wine[2];

    for (int j=3; j<=n; j++) {
        dp[j]= max(dp[j-2]+wine[j], dp[j-3] + wine[j-1] + wine[j]);
        dp[j] = max(dp[j-1], dp[j]);
    }

    cout << dp[n] << endl;
}