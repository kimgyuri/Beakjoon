#include <iostream>
#include <string>
using namespace std;

int N, R, G, B, dp[1002][3];

int main() {
    cin >> N;

    int home[3];

    for (int i=1; i<=N; i++) {
        cin >> R >> G >> B;
        home[0] = R;
        home[1] = G;
        home[2] = B;

        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home[0];
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home[1];
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + home[2];
    }

    cout << min(dp[N][0], min(dp[N][1], dp[N][2])) << endl;
}